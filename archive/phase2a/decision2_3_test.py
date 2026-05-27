"""
Decision 2+3 Test: Min-Words Threshold x Aggregation Strategy

Tests every combination of:
  - Min-words: 3, 5, 8, 10
  - Aggregation: 11 strategies (3A through 3K)
  - Thresholds: per-strategy variants

Two phases:
  1. COLLECT: Run pipeline, split sentences, run NLI. Saves to JSON.
     Expensive (~10-15 min). Run once.
  2. ANALYZE: Load JSON, apply all strategy combos, output report.
     Instant. Re-run freely after tweaking strategies.

Usage:
  python decision2_3_test.py --collect    # Phase 1: gather data
  python decision2_3_test.py --analyze    # Phase 2: test strategies
  python decision2_3_test.py --both       # Run both phases

Output:
  tests/decision2_3_data.json             # Collected NLI data
  tests/decision2_3_report.txt            # Analysis report

Place in project root (same level as app/).
"""

import asyncio
import argparse
import json
import os
import sys
import math
from datetime import datetime
from collections import defaultdict

import nltk
nltk.download('punkt_tab', quiet=True)
from nltk.tokenize import sent_tokenize

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# ============================================================
# CONFIGURATION
# ============================================================

SET_A_CLAIMS = [
    "vaccines cause autism",
    "the earth is flat",
    "humans only use 10 percent of their brain",
    "cracking your knuckles causes arthritis",
    "sugar makes children hyperactive",
    "the great wall of china is visible from space",
    "lightning never strikes the same place twice",
    "lemmings commit mass suicide",
    "climate change is caused by human activity",
    "smoking causes lung cancer",
    "the earth revolves around the sun",
    "the moon landing was faked",
    "5G towers cause cancer",
    "drinking bleach cures diseases",
    "nuclear energy is safe",
    "organic food is healthier than conventional food",
    "video games cause violence",
    "christopher columbus discovered america",
    "the average human body temperature is 98.6 degrees fahrenheit",
    "goldfish have a three second memory",
]

# Expected dominant stance for each claim's sources.
# "opposing" = claim is false, most sources debunk it
# "supporting" = claim is true, most sources confirm it
# "mixed" = contested, no single expected stance
EXPECTED_STANCE = {
    "vaccines cause autism": "opposing",
    "the earth is flat": "opposing",
    "humans only use 10 percent of their brain": "opposing",
    "cracking your knuckles causes arthritis": "opposing",
    "sugar makes children hyperactive": "opposing",
    "the great wall of china is visible from space": "opposing",
    "lightning never strikes the same place twice": "opposing",
    "lemmings commit mass suicide": "opposing",
    "climate change is caused by human activity": "supporting",
    "smoking causes lung cancer": "supporting",
    "the earth revolves around the sun": "supporting",
    "the moon landing was faked": "opposing",
    "5G towers cause cancer": "opposing",
    "drinking bleach cures diseases": "opposing",
    "nuclear energy is safe": "mixed",
    "organic food is healthier than conventional food": "mixed",
    "video games cause violence": "mixed",
    "christopher columbus discovered america": "opposing",
    "the average human body temperature is 98.6 degrees fahrenheit": "opposing",
    "goldfish have a three second memory": "opposing",
}

MIN_WORDS_OPTIONS = [3, 5, 8, 10]
THRESHOLD_OPTIONS = [0.4, 0.5, 0.6, 0.7, 0.8]

DATA_PATH = "tests/decision2_3_data.json"
REPORT_PATH = "tests/decision2_3_report.txt"


# ============================================================
# SENTENCE SPLITTING (from nli_service.py, Decision 1)
# ============================================================

import re

def _preprocess_for_splitting(text: str) -> str:
    text = re.sub(r'\bet al\.', 'et al', text)
    text = text.replace('B.o.B.', 'BoB')
    text = re.sub(r'\[edit\](\S)', r'[edit] \1', text)
    text = re.sub(r'\bNo\.\s*(\d)', r'No \1', text)
    return text


def split_sentences(text: str) -> list[str]:
    cleaned = _preprocess_for_splitting(text)
    return sent_tokenize(cleaned)


# ============================================================
# NLI MODEL (loaded only during collect phase)
# ============================================================

MODEL_NAME = "MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli"
LABEL_MAP = {0: "supporting", 1: "neutral", 2: "opposing"}

_model = None
_tokenizer = None


def _load_model():
    global _model, _tokenizer
    if _model is None:
        print(f"Loading {MODEL_NAME}...")
        _tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        _model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
        _model.eval()
        print("Model loaded.")


def _run_nli_batch(premises: list[str], hypothesis: str, batch_size: int = 32) -> list[dict]:
    """Batched NLI inference. Returns list of {p_supp, p_neut, p_opp, label, confidence}."""
    _load_model()
    results = []
    for i in range(0, len(premises), batch_size):
        batch_premises = premises[i:i+batch_size]
        batch_hypotheses = [hypothesis] * len(batch_premises)
        inputs = _tokenizer(
            batch_premises,
            batch_hypotheses,
            return_tensors="pt",
            truncation=True,
            max_length=512,
            padding=True,
        )
        with torch.no_grad():
            outputs = _model(**inputs)
        probs = torch.softmax(outputs.logits, dim=1)
        for j in range(len(batch_premises)):
            p = probs[j]
            idx = p.argmax().item()
            results.append({
                "p_supp": round(p[0].item(), 4),
                "p_neut": round(p[1].item(), 4),
                "p_opp": round(p[2].item(), 4),
                "label": LABEL_MAP[idx],
                "confidence": round(p[idx].item(), 4),
            })
    return results


# ============================================================
# COLLECT PHASE
# ============================================================

async def collect_data():
    """Run pipeline for all Set A claims, collect per-sentence NLI data."""
    from app.models.schemas import ClaimRequest
    from app.services.claim_service import search_sources, _filter_relevant_sources, _deduplicate_sources
    from app.services.claim_classifier import classify_claim_domain
    from app.services.source_router import build_routing_config

    all_data = []

    for ci, claim in enumerate(SET_A_CLAIMS):
        print(f"\n{'='*60}")
        print(f"CLAIM {ci+1}/{len(SET_A_CLAIMS)}: {claim}")
        print(f"{'='*60}")

        # Fetch sources through pipeline
        try:
            request = ClaimRequest(claim=claim)
            domain = classify_claim_domain(claim)
            routing = build_routing_config(domain, claim)
            raw = await search_sources(request, routing)
            raw = _filter_relevant_sources(claim, raw)
            raw = _deduplicate_sources(raw)
        except Exception as e:
            print(f"  ERROR fetching sources: {e}")
            continue

        # Filter to enriched sources (30+ words)
        sources = []
        for s in raw:
            snippet = s.snippet or ""
            if len(snippet.split()) >= 30:
                sources.append({
                    "title": s.title or "",
                    "snippet": snippet,
                    "source_type": s.source_type or "",
                    "url": s.url or "",
                })

        print(f"  Enriched sources: {len(sources)}")

        # Split sentences for all sources
        for si, source in enumerate(sources):
            sentences = split_sentences(source["snippet"])
            sentence_texts = [s.strip() for s in sentences if s.strip()]
            source["sentences"] = sentence_texts
            source["sentence_word_counts"] = [len(s.split()) for s in sentence_texts]

        # Run paragraph-level NLI for all sources (baseline)
        print(f"  Running paragraph-level NLI...")
        para_premises = [s["snippet"] for s in sources]
        if para_premises:
            para_results = _run_nli_batch(para_premises, claim)
            for si, source in enumerate(sources):
                source["paragraph_nli"] = para_results[si]

        # Run sentence-level NLI for all sentences across all sources
        # Collect all (sentence, source_index) pairs for batched inference
        all_sentences = []
        sentence_map = []  # (source_index, sentence_index)
        for si, source in enumerate(sources):
            for ji, sent in enumerate(source["sentences"]):
                all_sentences.append(sent)
                sentence_map.append((si, ji))

        print(f"  Running sentence-level NLI on {len(all_sentences)} sentences...")
        if all_sentences:
            sent_results = _run_nli_batch(all_sentences, claim)
            # Distribute results back to sources
            for source in sources:
                source["sentence_nli"] = []
            for idx, (si, ji) in enumerate(sentence_map):
                sources[si]["sentence_nli"].append(sent_results[idx])

        # Store
        for source in sources:
            all_data.append({
                "claim": claim,
                "expected_stance": EXPECTED_STANCE[claim],
                "title": source["title"],
                "source_type": source["source_type"],
                "url": source.get("url", ""),
                "word_count": len(source["snippet"].split()),
                "paragraph_nli": source.get("paragraph_nli", {}),
                "sentences": [
                    {
                        "text": source["sentences"][i],
                        "word_count": source["sentence_word_counts"][i],
                        **source["sentence_nli"][i],
                    }
                    for i in range(len(source["sentences"]))
                    if i < len(source.get("sentence_nli", []))
                ],
            })

    # Save
    os.makedirs("tests", exist_ok=True)
    with open(DATA_PATH, "w") as f:
        json.dump(all_data, f, indent=2)
    print(f"\nData saved to {DATA_PATH}")
    print(f"Total sources: {len(all_data)}")
    total_sents = sum(len(d["sentences"]) for d in all_data)
    print(f"Total sentences: {total_sents}")


# ============================================================
# AGGREGATION STRATEGIES
# ============================================================
# Each function takes:
#   sentences: list of dicts with {p_supp, p_neut, p_opp, text, word_count}
#   threshold: float (optional, for strategies that use one)
# Returns: (stance: str, confidence: float)

def agg_3A_strongest(sentences, **kwargs):
    """3A: Strongest non-neutral signal. Pick the single sentence
    with highest max(P_supp, P_opp)."""
    if not sentences:
        return "neutral", 0.5
    best = max(sentences, key=lambda s: max(s["p_supp"], s["p_opp"]))
    if best["p_supp"] > best["p_opp"]:
        return "supporting", best["p_supp"]
    else:
        return "opposing", best["p_opp"]


def agg_3B_gated_strongest(sentences, threshold=0.6, **kwargs):
    """3B: Confidence-gated strongest. Like 3A but only considers
    sentences above threshold. Falls back to neutral."""
    if not sentences:
        return "neutral", 0.5
    strong = [s for s in sentences if max(s["p_supp"], s["p_opp"]) > threshold]
    if not strong:
        return "neutral", 0.5
    return agg_3A_strongest(strong)


def agg_3C_score_sum(sentences, variant="sum", **kwargs):
    """3C: Score-based sum or mean. For each sentence: score = P(supp) - P(opp).
    Sum (or mean) all scores. Positive = supporting, negative = opposing."""
    if not sentences:
        return "neutral", 0.5
    scores = [s["p_supp"] - s["p_opp"] for s in sentences]
    if variant == "sum":
        total = sum(scores)
    else:
        total = sum(scores) / len(scores)
    if abs(total) < 0.01:
        return "neutral", 0.5
    if total > 0:
        return "supporting", min(abs(total) / max(len(scores) if variant == "sum" else 1, 1), 1.0)
    else:
        return "opposing", min(abs(total) / max(len(scores) if variant == "sum" else 1, 1), 1.0)


def agg_3C_score_mean(sentences, **kwargs):
    """3C variant: mean instead of sum."""
    return agg_3C_score_sum(sentences, variant="mean")


def agg_3D_relevance_weighted(sentences, claim_embedding=None, **kwargs):
    """3D: Relevance-weighted score sum. Each sentence's score weighted
    by its MiniLM relevance to the claim.
    NOTE: Requires relevance scores pre-computed and stored in sentence dicts.
    If not available, falls back to 3C."""
    if not sentences:
        return "neutral", 0.5
    if "relevance" not in sentences[0]:
        # Fallback: no relevance scores available, use unweighted
        return agg_3C_score_sum(sentences)
    weighted_scores = []
    total_weight = 0
    for s in sentences:
        score = s["p_supp"] - s["p_opp"]
        w = s["relevance"]
        weighted_scores.append(score * w)
        total_weight += w
    if total_weight < 0.001:
        return "neutral", 0.5
    avg = sum(weighted_scores) / total_weight
    if abs(avg) < 0.01:
        return "neutral", 0.5
    if avg > 0:
        return "supporting", min(abs(avg), 1.0)
    else:
        return "opposing", min(abs(avg), 1.0)


def agg_3E_max_with_count(sentences, threshold=0.6, **kwargs):
    """3E: Two-class max with count. If both directions have strong
    signals, defer to whichever has more sentences."""
    if not sentences:
        return "neutral", 0.5
    max_supp = max(s["p_supp"] for s in sentences)
    max_opp = max(s["p_opp"] for s in sentences)
    count_supp = sum(1 for s in sentences if s["p_supp"] > threshold)
    count_opp = sum(1 for s in sentences if s["p_opp"] > threshold)

    # Both directions have strong signals: defer to count
    if max_supp > threshold and max_opp > threshold:
        if count_supp > count_opp:
            return "supporting", max_supp * (count_supp / max(count_supp + count_opp, 1))
        elif count_opp > count_supp:
            return "opposing", max_opp * (count_opp / max(count_supp + count_opp, 1))
        else:
            # Tie: use stronger max
            if max_supp > max_opp:
                return "supporting", max_supp
            else:
                return "opposing", max_opp
    # Only one direction has strong signal
    elif max_supp > threshold:
        return "supporting", max_supp
    elif max_opp > threshold:
        return "opposing", max_opp
    else:
        return "neutral", max(max_supp, max_opp)


def agg_3F_count_vote(sentences, threshold=0.5, **kwargs):
    """3F: Count-weighted voting. Sum confidence for sentences classified
    in each direction. Whichever side has higher total wins."""
    if not sentences:
        return "neutral", 0.5
    supp_total = sum(s["p_supp"] for s in sentences if s["label"] == "supporting" and s["p_supp"] > threshold)
    opp_total = sum(s["p_opp"] for s in sentences if s["label"] == "opposing" and s["p_opp"] > threshold)
    supp_count = sum(1 for s in sentences if s["label"] == "supporting" and s["p_supp"] > threshold)
    opp_count = sum(1 for s in sentences if s["label"] == "opposing" and s["p_opp"] > threshold)

    if supp_total == 0 and opp_total == 0:
        return "neutral", 0.5
    if supp_total > opp_total:
        return "supporting", supp_total / max(supp_count, 1)
    elif opp_total > supp_total:
        return "opposing", opp_total / max(opp_count, 1)
    else:
        return "neutral", 0.5


def agg_3G_filtered_score_sum(sentences, threshold=0.5, **kwargs):
    """3G: Filtered score sum. Like 3C but only includes sentences
    where max(P_supp, P_opp) > threshold. Filters neutral mass."""
    if not sentences:
        return "neutral", 0.5
    strong = [s for s in sentences if max(s["p_supp"], s["p_opp"]) > threshold]
    if not strong:
        return "neutral", 0.5
    scores = [s["p_supp"] - s["p_opp"] for s in strong]
    total = sum(scores)
    if abs(total) < 0.01:
        return "neutral", 0.5
    if total > 0:
        return "supporting", min(abs(total) / len(strong), 1.0)
    else:
        return "opposing", min(abs(total) / len(strong), 1.0)


def agg_3H_majority_strong(sentences, threshold=0.6, **kwargs):
    """3H: Majority of strong signals. Among sentences with strong
    non-neutral signal, which direction has more? Pure count."""
    if not sentences:
        return "neutral", 0.5
    supp_count = sum(1 for s in sentences if s["p_supp"] > threshold)
    opp_count = sum(1 for s in sentences if s["p_opp"] > threshold)
    total_strong = supp_count + opp_count
    if total_strong == 0:
        return "neutral", 0.5
    if supp_count > opp_count:
        return "supporting", supp_count / total_strong
    elif opp_count > supp_count:
        return "opposing", opp_count / total_strong
    else:
        return "neutral", 0.5


def agg_3I_median(sentences, **kwargs):
    """3I: Median of score distribution. score = P(supp) - P(opp) per
    sentence. Take median. Resistant to outliers."""
    if not sentences:
        return "neutral", 0.5
    scores = sorted([s["p_supp"] - s["p_opp"] for s in sentences])
    n = len(scores)
    if n % 2 == 1:
        median = scores[n // 2]
    else:
        median = (scores[n // 2 - 1] + scores[n // 2]) / 2
    if abs(median) < 0.01:
        return "neutral", 0.5
    if median > 0:
        return "supporting", min(abs(median), 1.0)
    else:
        return "opposing", min(abs(median), 1.0)


def agg_3J_topk(sentences, k=3, **kwargs):
    """3J: Top-K comparison. Average the K strongest supporting and K
    strongest opposing signals. Compare averages."""
    if not sentences:
        return "neutral", 0.5
    # Sort by each direction's confidence
    by_supp = sorted(sentences, key=lambda s: s["p_supp"], reverse=True)
    by_opp = sorted(sentences, key=lambda s: s["p_opp"], reverse=True)
    k_actual = min(k, len(sentences))
    avg_supp = sum(s["p_supp"] for s in by_supp[:k_actual]) / k_actual
    avg_opp = sum(s["p_opp"] for s in by_opp[:k_actual]) / k_actual
    if abs(avg_supp - avg_opp) < 0.01:
        return "neutral", 0.5
    if avg_supp > avg_opp:
        return "supporting", avg_supp
    else:
        return "opposing", avg_opp


def agg_3K_bayesian(sentences, prior=0.5, **kwargs):
    """3K: Bayesian update. Start with equal prior for supporting/opposing.
    Each sentence updates the posterior using its P(supp) and P(opp) as
    likelihood ratios."""
    if not sentences:
        return "neutral", 0.5
    # Work in log-odds to avoid underflow
    # log_odds = log(P(supp) / P(opp))
    # Start at 0 (equal odds)
    log_odds = 0.0
    for s in sentences:
        p_s = max(s["p_supp"], 1e-6)
        p_o = max(s["p_opp"], 1e-6)
        log_odds += math.log(p_s / p_o)
    # Convert back to probability
    # P(supp) = sigmoid(log_odds)
    prob_supp = 1.0 / (1.0 + math.exp(-log_odds)) if abs(log_odds) < 500 else (1.0 if log_odds > 0 else 0.0)
    if abs(prob_supp - 0.5) < 0.01:
        return "neutral", 0.5
    if prob_supp > 0.5:
        return "supporting", prob_supp
    else:
        return "opposing", 1.0 - prob_supp


# Registry of all strategies with their parameter variants
STRATEGIES = {
    "3A_strongest": {
        "fn": agg_3A_strongest,
        "variants": [{}],
    },
    "3B_gated_t0.5": {"fn": agg_3B_gated_strongest, "variants": [{"threshold": 0.5}]},
    "3B_gated_t0.6": {"fn": agg_3B_gated_strongest, "variants": [{"threshold": 0.6}]},
    "3B_gated_t0.7": {"fn": agg_3B_gated_strongest, "variants": [{"threshold": 0.7}]},
    "3B_gated_t0.8": {"fn": agg_3B_gated_strongest, "variants": [{"threshold": 0.8}]},
    "3C_score_sum": {"fn": agg_3C_score_sum, "variants": [{}]},
    "3C_score_mean": {"fn": agg_3C_score_mean, "variants": [{}]},
    "3D_relevance_weighted": {"fn": agg_3D_relevance_weighted, "variants": [{}]},
    "3E_max_count_t0.5": {"fn": agg_3E_max_with_count, "variants": [{"threshold": 0.5}]},
    "3E_max_count_t0.6": {"fn": agg_3E_max_with_count, "variants": [{"threshold": 0.6}]},
    "3E_max_count_t0.7": {"fn": agg_3E_max_with_count, "variants": [{"threshold": 0.7}]},
    "3F_count_vote_t0.5": {"fn": agg_3F_count_vote, "variants": [{"threshold": 0.5}]},
    "3F_count_vote_t0.6": {"fn": agg_3F_count_vote, "variants": [{"threshold": 0.6}]},
    "3F_count_vote_t0.7": {"fn": agg_3F_count_vote, "variants": [{"threshold": 0.7}]},
    "3G_filtered_sum_t0.4": {"fn": agg_3G_filtered_score_sum, "variants": [{"threshold": 0.4}]},
    "3G_filtered_sum_t0.5": {"fn": agg_3G_filtered_score_sum, "variants": [{"threshold": 0.5}]},
    "3G_filtered_sum_t0.6": {"fn": agg_3G_filtered_score_sum, "variants": [{"threshold": 0.6}]},
    "3G_filtered_sum_t0.7": {"fn": agg_3G_filtered_score_sum, "variants": [{"threshold": 0.7}]},
    "3H_majority_t0.5": {"fn": agg_3H_majority_strong, "variants": [{"threshold": 0.5}]},
    "3H_majority_t0.6": {"fn": agg_3H_majority_strong, "variants": [{"threshold": 0.6}]},
    "3H_majority_t0.7": {"fn": agg_3H_majority_strong, "variants": [{"threshold": 0.7}]},
    "3H_majority_t0.8": {"fn": agg_3H_majority_strong, "variants": [{"threshold": 0.8}]},
    "3I_median": {"fn": agg_3I_median, "variants": [{}]},
    "3J_topk_k2": {"fn": agg_3J_topk, "variants": [{"k": 2}]},
    "3J_topk_k3": {"fn": agg_3J_topk, "variants": [{"k": 3}]},
    "3J_topk_k5": {"fn": agg_3J_topk, "variants": [{"k": 5}]},
    "3K_bayesian": {"fn": agg_3K_bayesian, "variants": [{}]},
}


# ============================================================
# PATTERN DETECTION
# ============================================================

def detect_pattern(sentences, threshold=0.6):
    """Auto-detect which pattern a source matches based on per-sentence NLI.

    Patterns:
      A_debunking: has supporting AND opposing strong signals, more opposing
      B_skeptic_quote: has supporting AND opposing strong signals, more supporting
      C_neutral_heavy: >70% neutral, sparse non-neutral signals
      D_all_neutral: paragraph non-neutral but zero strong sentence signals
      E_uniform: all non-neutral sentences point same direction
      F_gradual: no strong signals but many weak signals in same direction
    """
    if not sentences:
        return "empty"

    strong_supp = [s for s in sentences if s["p_supp"] > threshold]
    strong_opp = [s for s in sentences if s["p_opp"] > threshold]
    neutral_count = sum(1 for s in sentences if s["label"] == "neutral")
    neutral_pct = neutral_count / len(sentences)

    has_both = len(strong_supp) > 0 and len(strong_opp) > 0

    if has_both and len(strong_opp) > len(strong_supp):
        return "A_debunking"
    elif has_both and len(strong_supp) >= len(strong_opp):
        return "B_skeptic_quote"
    elif neutral_pct > 0.70 and (len(strong_supp) + len(strong_opp)) <= 2:
        return "C_neutral_heavy"
    elif len(strong_supp) == 0 and len(strong_opp) == 0:
        # Check for gradual signal
        scores = [s["p_supp"] - s["p_opp"] for s in sentences]
        positive = sum(1 for sc in scores if sc > 0.05)
        negative = sum(1 for sc in scores if sc < -0.05)
        if positive > len(sentences) * 0.5 and negative < 3:
            return "F_gradual_supp"
        elif negative > len(sentences) * 0.5 and positive < 3:
            return "F_gradual_opp"
        return "D_no_signal"
    elif len(strong_supp) > 0 and len(strong_opp) == 0:
        return "E_uniform_supp"
    elif len(strong_opp) > 0 and len(strong_supp) == 0:
        return "E_uniform_opp"
    else:
        return "unknown"


# ============================================================
# ANALYZE PHASE
# ============================================================

def analyze_data():
    """Load collected data, test all (min_words, strategy) combos, output report."""
    with open(DATA_PATH) as f:
        all_data = json.load(f)

    print(f"Loaded {len(all_data)} sources from {DATA_PATH}")

    out = []
    out.append(f"Decision 2+3 Analysis Report")
    out.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    out.append(f"Sources: {len(all_data)}")
    out.append(f"Claims: {len(set(d['claim'] for d in all_data))}")
    out.append(f"Min-words options: {MIN_WORDS_OPTIONS}")
    out.append(f"Strategies: {len(STRATEGIES)}")
    out.append("")

    # --------------------------------------------------------
    # SECTION 1: PATTERN DISTRIBUTION
    # --------------------------------------------------------
    out.append("=" * 90)
    out.append("SECTION 1: SOURCE PATTERN DISTRIBUTION")
    out.append("=" * 90)
    out.append("")

    pattern_counts = defaultdict(int)
    pattern_sources = defaultdict(list)
    for d in all_data:
        pat = detect_pattern(d["sentences"])
        pattern_counts[pat] += 1
        pattern_sources[pat].append(f"{d['claim'][:30]} | {d['title'][:40]}")

    for pat, count in sorted(pattern_counts.items(), key=lambda x: -x[1]):
        out.append(f"  {pat:25s}: {count:4d} ({100*count/len(all_data):.1f}%)")
    out.append("")

    # Show a few examples per pattern
    for pat in sorted(pattern_counts.keys()):
        out.append(f"  [{pat}] examples:")
        for ex in pattern_sources[pat][:3]:
            out.append(f"    - {ex}")
        out.append("")

    # --------------------------------------------------------
    # SECTION 2: PARAGRAPH-LEVEL BASELINE
    # --------------------------------------------------------
    out.append("=" * 90)
    out.append("SECTION 2: PARAGRAPH-LEVEL BASELINE")
    out.append("=" * 90)
    out.append("")

    # Only score sources with clear expected stance (not "mixed")
    scoreable = [d for d in all_data if d["expected_stance"] != "mixed"]
    para_correct = 0
    para_neutral = 0
    for d in scoreable:
        para_label = d["paragraph_nli"].get("label", "neutral")
        if para_label == d["expected_stance"]:
            para_correct += 1
        elif para_label == "neutral":
            para_neutral += 1

    out.append(f"  Scoreable sources (non-mixed claims): {len(scoreable)}")
    out.append(f"  Paragraph-level correct: {para_correct}/{len(scoreable)} ({100*para_correct/max(len(scoreable),1):.1f}%)")
    out.append(f"  Paragraph-level neutral (missed): {para_neutral}/{len(scoreable)} ({100*para_neutral/max(len(scoreable),1):.1f}%)")
    out.append(f"  Paragraph-level wrong direction: {len(scoreable)-para_correct-para_neutral}/{len(scoreable)}")
    out.append("")

    # --------------------------------------------------------
    # SECTION 3: STRATEGY COMPARISON GRID
    # --------------------------------------------------------
    out.append("=" * 90)
    out.append("SECTION 3: STRATEGY COMPARISON GRID")
    out.append("=" * 90)
    out.append("")
    out.append("Each cell: (correct / scoreable) on sources with clear expected stance.")
    out.append("'neutral' counts as INCORRECT (the source has a clear stance we should detect).")
    out.append("")

    # Run all combos
    results_grid = {}  # (min_words, strategy_name) -> {correct, neutral, wrong, total, per_pattern}

    for mw in MIN_WORDS_OPTIONS:
        for strat_name, strat_info in STRATEGIES.items():
            fn = strat_info["fn"]
            for variant_kwargs in strat_info["variants"]:
                key = (mw, strat_name)
                correct = 0
                neutral_miss = 0
                wrong_dir = 0
                per_pattern = defaultdict(lambda: {"correct": 0, "total": 0})

                for d in scoreable:
                    # Apply min-words filter
                    filtered = [s for s in d["sentences"] if s["word_count"] >= mw]
                    if not filtered:
                        # No sentences pass filter, default to neutral
                        predicted = "neutral"
                    else:
                        predicted, conf = fn(filtered, **variant_kwargs)

                    pat = detect_pattern(d["sentences"])
                    per_pattern[pat]["total"] += 1

                    if predicted == d["expected_stance"]:
                        correct += 1
                        per_pattern[pat]["correct"] += 1
                    elif predicted == "neutral":
                        neutral_miss += 1
                    else:
                        wrong_dir += 1

                results_grid[key] = {
                    "correct": correct,
                    "neutral_miss": neutral_miss,
                    "wrong_dir": wrong_dir,
                    "total": len(scoreable),
                    "accuracy": correct / max(len(scoreable), 1),
                    "per_pattern": dict(per_pattern),
                }

    # Sort by accuracy
    ranked = sorted(results_grid.items(), key=lambda x: -x[1]["accuracy"])

    # Top 20
    out.append("TOP 20 CONFIGURATIONS:")
    out.append(f"{'Rank':<5} {'MinW':<5} {'Strategy':<28} {'Correct':>8} {'Neutral':>8} {'Wrong':>8} {'Acc':>8}")
    out.append("-" * 80)
    for rank, (key, res) in enumerate(ranked[:20], 1):
        mw, strat = key
        out.append(f"{rank:<5} {mw:<5} {strat:<28} {res['correct']:>5}/{res['total']:<3} {res['neutral_miss']:>7} {res['wrong_dir']:>7} {100*res['accuracy']:>7.1f}%")
    out.append("")

    # Bottom 10
    out.append("BOTTOM 10 CONFIGURATIONS:")
    out.append(f"{'Rank':<5} {'MinW':<5} {'Strategy':<28} {'Correct':>8} {'Neutral':>8} {'Wrong':>8} {'Acc':>8}")
    out.append("-" * 80)
    for rank, (key, res) in enumerate(ranked[-10:], len(ranked) - 9):
        mw, strat = key
        out.append(f"{rank:<5} {mw:<5} {strat:<28} {res['correct']:>5}/{res['total']:<3} {res['neutral_miss']:>7} {res['wrong_dir']:>7} {100*res['accuracy']:>7.1f}%")
    out.append("")

    # --------------------------------------------------------
    # SECTION 4: PER-PATTERN BREAKDOWN FOR TOP 5
    # --------------------------------------------------------
    out.append("=" * 90)
    out.append("SECTION 4: PER-PATTERN BREAKDOWN (TOP 5 STRATEGIES)")
    out.append("=" * 90)
    out.append("")

    all_patterns = sorted(pattern_counts.keys())
    for rank, (key, res) in enumerate(ranked[:5], 1):
        mw, strat = key
        out.append(f"  #{rank}: mw={mw}, {strat} (overall {100*res['accuracy']:.1f}%)")
        for pat in all_patterns:
            pp = res["per_pattern"].get(pat, {"correct": 0, "total": 0})
            if pp["total"] > 0:
                pct = 100 * pp["correct"] / pp["total"]
                out.append(f"    {pat:25s}: {pp['correct']:3d}/{pp['total']:<3d} ({pct:.0f}%)")
        out.append("")

    # --------------------------------------------------------
    # SECTION 5: MIN-WORDS IMPACT (averaged across strategies)
    # --------------------------------------------------------
    out.append("=" * 90)
    out.append("SECTION 5: MIN-WORDS IMPACT")
    out.append("=" * 90)
    out.append("")
    out.append("Average accuracy across all strategies, per min-words value:")
    out.append("")

    for mw in MIN_WORDS_OPTIONS:
        accs = [res["accuracy"] for (m, s), res in results_grid.items() if m == mw]
        avg_acc = sum(accs) / len(accs) if accs else 0
        best = max(accs) if accs else 0
        worst = min(accs) if accs else 0
        out.append(f"  min_words={mw:2d}: avg={100*avg_acc:.1f}%  best={100*best:.1f}%  worst={100*worst:.1f}%")
    out.append("")

    # --------------------------------------------------------
    # SECTION 6: STRATEGY IMPACT (averaged across min-words)
    # --------------------------------------------------------
    out.append("=" * 90)
    out.append("SECTION 6: STRATEGY IMPACT (averaged across min-words)")
    out.append("=" * 90)
    out.append("")

    strat_avg = {}
    for strat_name in STRATEGIES:
        accs = [res["accuracy"] for (m, s), res in results_grid.items() if s == strat_name]
        strat_avg[strat_name] = sum(accs) / len(accs) if accs else 0
    for strat, avg in sorted(strat_avg.items(), key=lambda x: -x[1]):
        out.append(f"  {strat:<28s}: {100*avg:.1f}%")
    out.append("")

    # --------------------------------------------------------
    # SECTION 7: DETAILED DISAGREEMENT ANALYSIS
    # --------------------------------------------------------
    out.append("=" * 90)
    out.append("SECTION 7: SOURCES WHERE TOP STRATEGIES DISAGREE")
    out.append("=" * 90)
    out.append("")
    out.append("Shows sources where the top 3 strategies produce different stances.")
    out.append("Helps identify which strategy is actually correct on contested cases.")
    out.append("")

    top3_keys = [k for k, _ in ranked[:3]]
    top3_names = [f"mw={k[0]},{k[1]}" for k in top3_keys]

    for d in scoreable:
        predictions = []
        for key in top3_keys:
            mw, strat_name = key
            fn = STRATEGIES[strat_name]["fn"]
            variant_kwargs = STRATEGIES[strat_name]["variants"][0]
            filtered = [s for s in d["sentences"] if s["word_count"] >= mw]
            if not filtered:
                predictions.append("neutral")
            else:
                pred, conf = fn(filtered, **variant_kwargs)
                predictions.append(pred)

        # Only show if they disagree
        if len(set(predictions)) > 1:
            pat = detect_pattern(d["sentences"])
            out.append(f"  Claim: {d['claim']}")
            out.append(f"  Source: {d['title'][:70]}")
            out.append(f"  Pattern: {pat}")
            out.append(f"  Expected: {d['expected_stance']}")
            out.append(f"  Paragraph: {d['paragraph_nli'].get('label', '?')}")
            for i, key in enumerate(top3_keys):
                out.append(f"  {top3_names[i]:>40s}: {predictions[i]}")

            # Show top 3 strongest sentences for context
            non_neutral = sorted(
                [s for s in d["sentences"] if s["label"] != "neutral"],
                key=lambda s: max(s["p_supp"], s["p_opp"]),
                reverse=True,
            )
            if non_neutral:
                out.append(f"  Top non-neutral sentences:")
                for s in non_neutral[:3]:
                    out.append(f"    [{s['label']:10s} S:{s['p_supp']:.3f} O:{s['p_opp']:.3f}] {s['text'][:100]}")
            out.append("")

    # --------------------------------------------------------
    # SECTION 8: PARAGRAPH vs BEST SENTENCE-LEVEL
    # --------------------------------------------------------
    out.append("=" * 90)
    out.append("SECTION 8: PARAGRAPH vs BEST SENTENCE-LEVEL")
    out.append("=" * 90)
    out.append("")

    best_key, best_res = ranked[0]
    best_mw, best_strat = best_key
    best_fn = STRATEGIES[best_strat]["fn"]
    best_kwargs = STRATEGIES[best_strat]["variants"][0]

    para_only = 0   # paragraph correct, sentence wrong
    sent_only = 0   # sentence correct, paragraph wrong
    both_correct = 0
    both_wrong = 0

    para_only_examples = []
    sent_only_examples = []

    for d in scoreable:
        para_label = d["paragraph_nli"].get("label", "neutral")
        filtered = [s for s in d["sentences"] if s["word_count"] >= best_mw]
        if filtered:
            sent_label, _ = best_fn(filtered, **best_kwargs)
        else:
            sent_label = "neutral"

        para_ok = (para_label == d["expected_stance"])
        sent_ok = (sent_label == d["expected_stance"])

        if para_ok and sent_ok:
            both_correct += 1
        elif para_ok and not sent_ok:
            para_only += 1
            para_only_examples.append(f"  {d['claim'][:30]} | {d['title'][:40]} | sent={sent_label}")
        elif not para_ok and sent_ok:
            sent_only += 1
            sent_only_examples.append(f"  {d['claim'][:30]} | {d['title'][:40]} | para={para_label}")
        else:
            both_wrong += 1

    out.append(f"  Best sentence config: mw={best_mw}, {best_strat}")
    out.append(f"  Both correct:          {both_correct}")
    out.append(f"  Only paragraph correct: {para_only} (sentence-level REGRESSIONS)")
    out.append(f"  Only sentence correct:  {sent_only} (sentence-level WINS)")
    out.append(f"  Both wrong:            {both_wrong}")
    out.append(f"  Net improvement:       {sent_only - para_only:+d}")
    out.append("")

    if para_only_examples:
        out.append("  REGRESSIONS (paragraph correct, sentence wrong):")
        for ex in para_only_examples[:10]:
            out.append(f"    {ex}")
        out.append("")

    if sent_only_examples:
        out.append("  WINS (sentence correct, paragraph wrong):")
        for ex in sent_only_examples[:10]:
            out.append(f"    {ex}")
        out.append("")

    # Write report
    os.makedirs("tests", exist_ok=True)
    with open(REPORT_PATH, "w") as f:
        f.write("\n".join(out))
    print(f"\nReport written to {REPORT_PATH}")
    print(f"\nQuick summary:")
    print(f"  Paragraph baseline: {para_correct}/{len(scoreable)} ({100*para_correct/max(len(scoreable),1):.1f}%)")
    mw, strat = ranked[0][0]
    res = ranked[0][1]
    print(f"  Best config: mw={mw}, {strat}: {res['correct']}/{res['total']} ({100*res['accuracy']:.1f}%)")
    print(f"  Net improvement over paragraph: {sent_only - para_only:+d} sources")
    print(f"\n  Top 5:")
    for rank, (key, res) in enumerate(ranked[:5], 1):
        mw, strat = key
        print(f"    #{rank}: mw={mw}, {strat} = {100*res['accuracy']:.1f}%")


# ============================================================
# MAIN
# ============================================================

def main():
    parser = argparse.ArgumentParser(description="Decision 2+3 Test")
    parser.add_argument("--collect", action="store_true", help="Run collect phase (expensive)")
    parser.add_argument("--analyze", action="store_true", help="Run analyze phase (instant)")
    parser.add_argument("--both", action="store_true", help="Run both phases")
    args = parser.parse_args()

    if not (args.collect or args.analyze or args.both):
        print("Usage:")
        print("  python decision2_3_test.py --collect    # Phase 1: gather NLI data (~10-15 min)")
        print("  python decision2_3_test.py --analyze    # Phase 2: test strategies (instant)")
        print("  python decision2_3_test.py --both       # Run both")
        sys.exit(1)

    if args.collect or args.both:
        asyncio.run(collect_data())

    if args.analyze or args.both:
        if not os.path.exists(DATA_PATH):
            print(f"ERROR: {DATA_PATH} not found. Run --collect first.")
            sys.exit(1)
        analyze_data()


if __name__ == "__main__":
    main()