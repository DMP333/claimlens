"""
Phase 2 Validation: Set B + Additional Unseen Claims

Runs REAL pipeline calls (source search, enrichment, sentence-level NLI)
on held-back claims never used during Phase 2 development.

Two phases:
  1. COLLECT: Run pipeline for each claim, save all data. (~30-60 min)
  2. ANALYZE: Load data, compute verdicts, diagnose errors. (instant)

Reports:
  - Overall accuracy (all, seen-in-Set-A, truly-unseen)
  - Per-strategy comparison (3K, 3A, 3J)
  - Per-category breakdown (factual_true, factual_false, opinion, contested)
  - Sentence-level error patterns for fine-tuning planning
  - Phase 1 paragraph-level vs Phase 2 sentence-level comparison

Usage:
  python validation_setb.py --collect
  python validation_setb.py --analyze
  python validation_setb.py --both

Output:
  tests/validation_data.json
  tests/validation_report.txt
"""

import asyncio
import argparse
import json
import os
import sys
import math
import re
from datetime import datetime
from collections import defaultdict, Counter

DATA_PATH = "tests/validation_data.json"
REPORT_PATH = "tests/validation_report.txt"

# ============================================================
# CLAIMS: Set B (36) + Additional Unseen (12) = 48 total
# ============================================================

# Claims that overlap with Set A (Phase 2 development set)
SEEN_CLAIMS = {
    "the earth is flat",
    "vaccines cause autism",
    "the moon landing was faked",
    "nuclear energy is safe",
    "smoking causes lung cancer",
    "goldfish have a 3 second memory",
    "the Great Wall of China is visible from space",
    "organic food is healthier than conventional food",
    "the Great Wall of China is the only man-made structure visible from space",
    "we only use 10% of our brains",
    "violent video games cause real world violence",
}

VALIDATION_CLAIMS = [
    # === SET B (36 claims from Phase 1 baseline) ===
    # Factual true
    {"claim": "climate change is real", "expected": "strongly supported", "category": "factual_true"},
    {"claim": "evolution is real", "expected": "strongly supported", "category": "factual_true"},
    {"claim": "water boils at 100 degrees celsius", "expected": "strongly supported", "category": "factual_true"},
    {"claim": "the speed of light is constant", "expected": "strongly supported", "category": "factual_true"},
    {"claim": "smoking causes lung cancer", "expected": "strongly supported", "category": "factual_true"},
    {"claim": "antibiotics do not work against viruses", "expected": "strongly supported", "category": "factual_true"},
    {"claim": "humans share about 98% of DNA with chimpanzees", "expected": "strongly supported", "category": "factual_true"},

    # Factual false
    {"claim": "the earth is flat", "expected": "strongly opposed", "category": "factual_false"},
    {"claim": "vaccines cause autism", "expected": "strongly opposed", "category": "factual_false"},
    {"claim": "the moon landing was faked", "expected": "strongly opposed", "category": "factual_false"},
    {"claim": "5G causes COVID", "expected": "strongly opposed", "category": "factual_false"},
    {"claim": "we only use 10% of our brains", "expected": "strongly opposed", "category": "factual_false"},
    {"claim": "goldfish have a 3 second memory", "expected": "strongly opposed", "category": "factual_false"},
    {"claim": "the Great Wall of China is visible from space", "expected": "strongly opposed", "category": "factual_false"},
    {"claim": "MSG is dangerous to consume", "expected": "strongly opposed", "category": "factual_false"},
    {"claim": "eating carrots improves your eyesight", "expected": "strongly opposed", "category": "factual_false"},
    {"claim": "the Amazon rainforest produces about 20% of the world's oxygen", "expected": "strongly opposed", "category": "factual_false"},
    {"claim": "the Great Wall of China is the only man-made structure visible from space", "expected": "strongly opposed", "category": "factual_false"},

    # Opinion
    {"claim": "LeBron James is the greatest basketball player of all time", "expected": "opinion", "category": "opinion"},
    {"claim": "pineapple belongs on pizza", "expected": "opinion", "category": "opinion"},
    {"claim": "democracy is the best form of government", "expected": "opinion", "category": "opinion"},
    {"claim": "capitalism is better than socialism", "expected": "opinion", "category": "opinion"},
    {"claim": "the Beatles are the greatest band of all time", "expected": "opinion", "category": "opinion"},
    {"claim": "cats are better pets than dogs", "expected": "opinion", "category": "opinion"},
    {"claim": "college education is worth the cost", "expected": "opinion", "category": "opinion"},

    # Contested
    {"claim": "sugar is worse than fat for health", "expected": "contested", "category": "contested"},
    {"claim": "nuclear energy is safe", "expected": "contested", "category": "contested"},
    {"claim": "remote work is more productive than office work", "expected": "contested", "category": "contested"},
    {"claim": "AI will replace most jobs", "expected": "contested", "category": "contested"},
    {"claim": "the United States economy is in a recession", "expected": "contested", "category": "contested"},
    {"claim": "violent video games cause real world violence", "expected": "contested", "category": "contested"},
    {"claim": "social media is harmful to mental health", "expected": "contested", "category": "contested"},
    {"claim": "organic food is healthier than conventional food", "expected": "contested", "category": "contested"},
    {"claim": "immigration is good for the economy", "expected": "contested", "category": "contested"},
    {"claim": "China has the world's largest economy", "expected": "contested", "category": "current_event"},
    {"claim": "inflation in the United States is under control", "expected": "contested", "category": "current_event"},

    # === ADDITIONAL UNSEEN (12 claims, none in Set A or audit) ===
    {"claim": "bats are blind", "expected": "strongly opposed", "category": "factual_false"},
    {"claim": "bulls are enraged by the color red", "expected": "strongly opposed", "category": "factual_false"},
    {"claim": "you lose most body heat through your head", "expected": "strongly opposed", "category": "factual_false"},
    {"claim": "shaving makes hair grow back thicker", "expected": "strongly opposed", "category": "factual_false"},
    {"claim": "the Sahara desert is the largest desert on earth", "expected": "strongly opposed", "category": "factual_false"},
    {"claim": "Einstein failed math in school", "expected": "strongly opposed", "category": "factual_false"},
    {"claim": "dogs can only see in black and white", "expected": "strongly opposed", "category": "factual_false"},
    {"claim": "the sun is a star", "expected": "strongly supported", "category": "factual_true"},
    {"claim": "octopuses have three hearts", "expected": "strongly supported", "category": "factual_true"},
    {"claim": "honey never expires", "expected": "strongly supported", "category": "factual_true"},
    {"claim": "universal basic income reduces poverty", "expected": "contested", "category": "contested"},
    {"claim": "cryptocurrency is a good long-term investment", "expected": "opinion", "category": "opinion"},
]


# ============================================================
# PIPELINE + NLI (from nli_service.py)
# ============================================================

import nltk
nltk.download('punkt_tab', quiet=True)
from nltk.tokenize import sent_tokenize
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

MODEL_NAME = "MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli"
LABEL_MAP = {0: "supporting", 1: "neutral", 2: "opposing"}
MIN_WORDS = 10

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

def _preprocess_for_splitting(text):
    text = re.sub(r'\bet al\.', 'et al', text)
    text = text.replace('B.o.B.', 'BoB')
    text = re.sub(r'\[edit\](\S)', r'[edit] \1', text)
    text = re.sub(r'\bNo\.\s*(\d)', r'No \1', text)
    return text

def _run_nli_batch(premises, hypothesis, batch_size=32):
    _load_model()
    results = []
    for i in range(0, len(premises), batch_size):
        batch = premises[i:i+batch_size]
        inputs = _tokenizer(batch, [hypothesis]*len(batch), return_tensors="pt",
                           truncation=True, max_length=512, padding=True)
        with torch.no_grad():
            outputs = _model(**inputs)
        probs = torch.softmax(outputs.logits, dim=1)
        for j in range(len(batch)):
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
    from app.models.schemas import ClaimRequest
    from app.services.claim_service import analyze_claim

    # Resume support
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH) as f:
            all_data = json.load(f)
        print(f"Resuming: {len(all_data)} claims already collected")
    else:
        all_data = []

    collected_claims = {d["claim"] for d in all_data}

    for ci, tc in enumerate(VALIDATION_CLAIMS):
        claim = tc["claim"]
        if claim in collected_claims:
            print(f"\n[{ci+1}/{len(VALIDATION_CLAIMS)}] SKIP (already collected): {claim}")
            continue

        print(f"\n{'='*60}")
        print(f"[{ci+1}/{len(VALIDATION_CLAIMS)}] {claim}")
        print(f"{'='*60}")

        try:
            # Run full pipeline (this uses sentence-level NLI via claim_service)
            result = await analyze_claim(ClaimRequest(claim=claim))

            # Also collect per-sentence data for error analysis
            # Re-run sentence splitting + NLI on non-FC sources for detailed data
            from app.services.claim_service import search_sources, _filter_relevant_sources, _deduplicate_sources
            from app.services.claim_classifier import classify_claim_domain
            from app.services.source_router import build_routing_config

            request = ClaimRequest(claim=claim)
            domain = classify_claim_domain(claim)
            routing = build_routing_config(domain, claim)
            raw = await search_sources(request, routing)
            raw = _filter_relevant_sources(claim, raw)
            raw = _deduplicate_sources(raw)

            # Collect sentence-level data for non-FC sources
            source_details = []
            for source in raw:
                snippet = source.snippet or ""
                if len(snippet.split()) < 30:
                    continue

                sentences = sent_tokenize(_preprocess_for_splitting(snippet))
                filtered = [(i, s) for i, s in enumerate(sentences) if len(s.split()) >= MIN_WORDS]

                if filtered:
                    texts = [s for _, s in filtered]
                    nli_results = _run_nli_batch(texts, claim)
                    sent_data = []
                    for (orig_idx, text), nli in zip(filtered, nli_results):
                        sent_data.append({
                            "text": text,
                            "word_count": len(text.split()),
                            **nli,
                        })
                else:
                    sent_data = []

                # Also run paragraph-level for comparison
                para_result = _run_nli_batch([snippet], claim)[0] if snippet else {}

                source_details.append({
                    "title": source.title or "",
                    "source_type": source.source_type or "",
                    "url": source.url or "",
                    "word_count": len(snippet.split()),
                    "paragraph_nli": para_result,
                    "sentences": sent_data,
                })

            entry = {
                "claim": claim,
                "expected": tc["expected"],
                "category": tc["category"],
                "seen_in_set_a": claim in SEEN_CLAIMS,
                "verdict": result.verdict,
                "confidence": result.confidence_in_verdict,
                "claim_type": result.claim_type,
                "num_sources": len(result.sources),
                "source_stances": [
                    {"stance": s.stance, "confidence": s.stance_confidence,
                     "title": s.title[:60], "summary": s.support_summary}
                    for s in result.sources
                ],
                "source_details": source_details,
            }
            all_data.append(entry)

        except Exception as e:
            print(f"  ERROR: {e}")
            import traceback
            traceback.print_exc()
            all_data.append({
                "claim": claim, "expected": tc["expected"],
                "category": tc["category"], "seen_in_set_a": claim in SEEN_CLAIMS,
                "verdict": "ERROR", "confidence": 0, "error": str(e),
                "source_details": [],
            })

        # Save after each claim (resume support)
        os.makedirs("tests", exist_ok=True)
        with open(DATA_PATH, "w") as f:
            json.dump(all_data, f, indent=2)

    print(f"\nData saved to {DATA_PATH}")
    print(f"Total claims: {len(all_data)}")


# ============================================================
# AGGREGATION STRATEGIES (for re-scoring during analysis)
# ============================================================

def agg_3k(sents):
    if not sents: return "neutral", 0.5
    lo = sum(math.log(max(s["p_supp"],1e-6)/max(s["p_opp"],1e-6)) for s in sents)
    if abs(lo)>500: p=1.0 if lo>0 else 0.0
    else: p=1.0/(1.0+math.exp(-lo))
    return ("supporting" if p>0.5 else "opposing"), (p if p>0.5 else 1.0-p)

def agg_3a(sents):
    if not sents: return "neutral", 0.5
    best = max(sents, key=lambda s: max(s["p_supp"], s["p_opp"]))
    return ("supporting" if best["p_supp"]>best["p_opp"] else "opposing"), max(best["p_supp"], best["p_opp"])

def agg_3j(sents, k=3):
    if not sents: return "neutral", 0.5
    k_a = min(k, len(sents))
    by_s = sorted(sents, key=lambda s: s["p_supp"], reverse=True)
    by_o = sorted(sents, key=lambda s: s["p_opp"], reverse=True)
    avg_s = sum(s["p_supp"] for s in by_s[:k_a])/k_a
    avg_o = sum(s["p_opp"] for s in by_o[:k_a])/k_a
    if abs(avg_s-avg_o)<0.01: return "neutral", 0.5
    return ("supporting" if avg_s>avg_o else "opposing"), max(avg_s, avg_o)

STRATEGIES = {"3K": agg_3k, "3A": agg_3a, "3J": agg_3j}


def compute_verdict_from_stances(stances_with_conf, claim_type):
    """Recompute pipeline verdict from per-source stances."""
    w_supp = sum(conf for stance, conf in stances_with_conf if stance == "supporting")
    w_opp = sum(conf for stance, conf in stances_with_conf if stance == "opposing")
    total = w_supp + w_opp
    if total == 0:
        return "insufficient evidence"
    ratio = w_supp / total
    if claim_type == "opinion":
        if ratio >= 0.60: return "sources lean supporting"
        elif ratio > 0.40: return "sources divided"
        else: return "sources lean opposing"
    if ratio >= 0.80: return "strongly supported"
    elif ratio >= 0.60: return "likely supported"
    elif ratio > 0.40: return "contested"
    elif ratio >= 0.20: return "likely opposed"
    else: return "strongly opposed"


def is_correct(verdict, expected):
    """Check if verdict matches expected, with fuzzy matching."""
    v, e = verdict.lower(), expected.lower()
    if "opinion" in e:
        return "sources" in v or "opinion" in v or "divided" in v
    if "supported" in e:
        return "supported" in v
    if "opposed" in e:
        return "opposed" in v
    if "contested" in e:
        return "contested" in v or "divided" in v or "insufficient" in v
    return v == e


# ============================================================
# ANALYZE PHASE
# ============================================================

def analyze_data():
    with open(DATA_PATH) as f:
        all_data = json.load(f)

    out = []
    out.append(f"Phase 2 Validation Report")
    out.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    out.append(f"Total claims: {len(all_data)}")
    seen = [d for d in all_data if d.get("seen_in_set_a")]
    unseen = [d for d in all_data if not d.get("seen_in_set_a")]
    out.append(f"Seen (in Set A): {len(seen)}")
    out.append(f"Unseen (truly held-back): {len(unseen)}")
    errors = [d for d in all_data if d.get("verdict") == "ERROR"]
    out.append(f"Errors (pipeline failed): {len(errors)}")
    out.append("")

    valid = [d for d in all_data if d.get("verdict") != "ERROR"]

    # ========================================
    # SECTION 1: PIPELINE VERDICT ACCURACY
    # ========================================
    out.append("=" * 80)
    out.append("SECTION 1: PIPELINE VERDICT ACCURACY (using default 3K strategy)")
    out.append("=" * 80)
    out.append("")

    for label, subset in [("ALL", valid), ("SEEN", [d for d in valid if d.get("seen_in_set_a")]),
                          ("UNSEEN", [d for d in valid if not d.get("seen_in_set_a")])]:
        correct = sum(1 for d in subset if is_correct(d["verdict"], d["expected"]))
        out.append(f"  {label:8s}: {correct}/{len(subset)} ({100*correct/max(len(subset),1):.1f}%)")
    out.append("")

    # Per-category
    out.append("  By category:")
    for cat in ["factual_true", "factual_false", "opinion", "contested", "current_event"]:
        subset = [d for d in valid if d["category"] == cat]
        if not subset:
            continue
        correct = sum(1 for d in subset if is_correct(d["verdict"], d["expected"]))
        out.append(f"    {cat:20s}: {correct}/{len(subset)} ({100*correct/max(len(subset),1):.1f}%)")
    out.append("")

    # Per-claim detail
    out.append("  Per-claim results:")
    for d in valid:
        ok = "OK" if is_correct(d["verdict"], d["expected"]) else "XX"
        seen_tag = "[SEEN]" if d.get("seen_in_set_a") else ""
        out.append(f"    {ok} {d['verdict']:25s} (exp: {d['expected']:20s}) | "
                   f"{d['claim'][:50]} {seen_tag}")
    out.append("")

    # ========================================
    # SECTION 2: STRATEGY COMPARISON
    # ========================================
    out.append("=" * 80)
    out.append("SECTION 2: STRATEGY COMPARISON (3K vs 3A vs 3J)")
    out.append("=" * 80)
    out.append("")

    # Re-score each claim with each strategy using source_details
    strat_results = {s: {"all": 0, "seen": 0, "unseen": 0,
                         "all_n": 0, "seen_n": 0, "unseen_n": 0} for s in STRATEGIES}

    for d in valid:
        if not d.get("source_details"):
            continue

        for strat_name, strat_fn in STRATEGIES.items():
            stances = []
            for src in d["source_details"]:
                sents = [s for s in src.get("sentences", []) if s["word_count"] >= MIN_WORDS]
                if sents:
                    stance, conf = strat_fn(sents)
                    stances.append((stance, conf))

            if stances:
                verdict = compute_verdict_from_stances(stances, d.get("claim_type", "factual"))
            else:
                verdict = "insufficient evidence"

            correct = is_correct(verdict, d["expected"])
            strat_results[strat_name]["all_n"] += 1
            if correct:
                strat_results[strat_name]["all"] += 1
            if d.get("seen_in_set_a"):
                strat_results[strat_name]["seen_n"] += 1
                if correct: strat_results[strat_name]["seen"] += 1
            else:
                strat_results[strat_name]["unseen_n"] += 1
                if correct: strat_results[strat_name]["unseen"] += 1

    out.append(f"  {'Strategy':<10s} {'All':>15s} {'Seen':>15s} {'Unseen':>15s}")
    out.append(f"  " + "-" * 60)
    for sname, sr in strat_results.items():
        a = f"{sr['all']}/{sr['all_n']} ({100*sr['all']/max(sr['all_n'],1):.0f}%)"
        s = f"{sr['seen']}/{sr['seen_n']} ({100*sr['seen']/max(sr['seen_n'],1):.0f}%)"
        u = f"{sr['unseen']}/{sr['unseen_n']} ({100*sr['unseen']/max(sr['unseen_n'],1):.0f}%)"
        out.append(f"  {sname:<10s} {a:>15s} {s:>15s} {u:>15s}")
    out.append("")

    # ========================================
    # SECTION 3: PARAGRAPH vs SENTENCE COMPARISON
    # ========================================
    out.append("=" * 80)
    out.append("SECTION 3: PARAGRAPH-LEVEL vs SENTENCE-LEVEL (per-source)")
    out.append("=" * 80)
    out.append("")

    para_correct = 0
    sent_correct = 0
    total_sources = 0
    para_only = 0
    sent_only = 0

    for d in valid:
        expected_source_stance = None
        if d["category"] == "factual_false":
            expected_source_stance = "opposing"
        elif d["category"] == "factual_true":
            expected_source_stance = "supporting"
        else:
            continue

        for src in d.get("source_details", []):
            sents = [s for s in src.get("sentences", []) if s["word_count"] >= MIN_WORDS]
            if not sents:
                continue
            total_sources += 1

            para_label = src.get("paragraph_nli", {}).get("label", "neutral")
            sent_stance, _ = agg_3k(sents)

            p_ok = para_label == expected_source_stance
            s_ok = sent_stance == expected_source_stance
            if p_ok: para_correct += 1
            if s_ok: sent_correct += 1
            if p_ok and not s_ok: para_only += 1
            if s_ok and not p_ok: sent_only += 1

    out.append(f"  Per-source accuracy (factual claims only, n={total_sources}):")
    out.append(f"    Paragraph-level: {para_correct}/{total_sources} ({100*para_correct/max(total_sources,1):.1f}%)")
    out.append(f"    Sentence-level (3K): {sent_correct}/{total_sources} ({100*sent_correct/max(total_sources,1):.1f}%)")
    out.append(f"    Only paragraph correct: {para_only}")
    out.append(f"    Only sentence correct: {sent_only}")
    out.append(f"    Net improvement: {sent_only - para_only:+d}")
    out.append("")

    # ========================================
    # SECTION 4: SENTENCE-LEVEL ERROR PATTERNS
    # ========================================
    out.append("=" * 80)
    out.append("SECTION 4: SENTENCE-LEVEL ERROR PATTERNS (for fine-tuning)")
    out.append("=" * 80)
    out.append("")

    myth_restating = []
    weak_negation_candidates = []
    no_signal_sources = []

    negation_words = {"no", "not", "never", "none", "neither", "nor", "nothing",
                      "without", "lack", "failed", "unable", "unlikely",
                      "disproven", "debunked", "refuted", "myth", "false",
                      "incorrect", "wrong", "flawed", "unsupported"}

    for d in valid:
        if d["category"] not in ("factual_false", "factual_true"):
            continue

        expected_stance = "opposing" if d["category"] == "factual_false" else "supporting"

        for src in d.get("source_details", []):
            sents = [s for s in src.get("sentences", []) if s["word_count"] >= MIN_WORDS]
            if not sents:
                continue

            # Check for no-signal sources
            n_nonneutral = sum(1 for s in sents if s["label"] != "neutral")
            if n_nonneutral == 0:
                no_signal_sources.append({
                    "claim": d["claim"][:40],
                    "title": src["title"][:50],
                    "num_sents": len(sents),
                })

            for s in sents:
                # Myth-restating: supporting classification on false-claim source
                if (d["category"] == "factual_false" and
                    s["label"] == "supporting" and s["p_supp"] > 0.7):
                    myth_restating.append({
                        "claim": d["claim"][:40],
                        "title": src["title"][:40],
                        "text": s["text"][:120],
                        "p_supp": s["p_supp"],
                    })

                # Weak negation: has negation words but classified as neutral
                if (s["label"] == "neutral" and expected_stance == "opposing"):
                    words = set(s["text"].lower().split())
                    neg_found = words & negation_words
                    if neg_found and s["p_opp"] > 0.1:
                        weak_negation_candidates.append({
                            "claim": d["claim"][:40],
                            "text": s["text"][:120],
                            "neg_words": list(neg_found),
                            "p_opp": s["p_opp"],
                            "p_neut": s["p_neut"],
                        })

    out.append(f"  MYTH-RESTATING SENTENCES: {len(myth_restating)}")
    out.append(f"  (False-claim debunking sources where NLI reads myth setup as 'supporting')")
    for mr in myth_restating[:15]:
        out.append(f"    [S:{mr['p_supp']:.3f}] {mr['claim']} | {mr['text'][:90]}")
    if len(myth_restating) > 15:
        out.append(f"    ... and {len(myth_restating)-15} more")
    out.append("")

    out.append(f"  WEAK NEGATION CANDIDATES: {len(weak_negation_candidates)}")
    out.append(f"  (Sentences with negation words classified as neutral, expected opposing)")
    for wn in sorted(weak_negation_candidates, key=lambda x: -x["p_opp"])[:15]:
        out.append(f"    [O:{wn['p_opp']:.3f} N:{wn['p_neut']:.3f}] neg={wn['neg_words']} | {wn['text'][:80]}")
    if len(weak_negation_candidates) > 15:
        out.append(f"    ... and {len(weak_negation_candidates)-15} more")
    out.append("")

    out.append(f"  NO-SIGNAL SOURCES: {len(no_signal_sources)}")
    out.append(f"  (All sentences classified neutral, no stance signal at all)")
    for ns in no_signal_sources[:10]:
        out.append(f"    {ns['claim']} | {ns['title']} ({ns['num_sents']} sents)")
    if len(no_signal_sources) > 10:
        out.append(f"    ... and {len(no_signal_sources)-10} more")
    out.append("")

    # ========================================
    # SECTION 5: FAILURES - DETAILED DIAGNOSIS
    # ========================================
    out.append("=" * 80)
    out.append("SECTION 5: WRONG VERDICTS - DETAILED DIAGNOSIS")
    out.append("=" * 80)
    out.append("")

    for d in valid:
        if is_correct(d["verdict"], d["expected"]):
            continue
        out.append(f"  WRONG: {d['claim']}")
        out.append(f"    Got: {d['verdict']} | Expected: {d['expected']} | Category: {d['category']}")
        out.append(f"    Sources: {d.get('num_sources', 0)}")
        seen_tag = " [SEEN]" if d.get("seen_in_set_a") else ""
        out.append(f"    Set: {'Set A overlap' if d.get('seen_in_set_a') else 'Truly unseen'}{seen_tag}")

        # Show source stance distribution
        if d.get("source_stances"):
            stance_dist = Counter(s["stance"] for s in d["source_stances"])
            out.append(f"    Source stances: {dict(stance_dist)}")

        # Show sentence-level detail for first 2 sources
        for src in d.get("source_details", [])[:2]:
            sents = [s for s in src.get("sentences", []) if s["word_count"] >= MIN_WORDS]
            if not sents:
                continue
            n_s = sum(1 for s in sents if s["label"] == "supporting")
            n_o = sum(1 for s in sents if s["label"] == "opposing")
            n_n = sum(1 for s in sents if s["label"] == "neutral")
            out.append(f"    Source: {src['title'][:50]} | S:{n_s} N:{n_n} O:{n_o}")
            # Show strongest non-neutral sentence
            nonneutral = [s for s in sents if s["label"] != "neutral"]
            if nonneutral:
                best = max(nonneutral, key=lambda s: max(s["p_supp"], s["p_opp"]))
                out.append(f"      Top: [{best['label'][:3]} {max(best['p_supp'],best['p_opp']):.3f}] {best['text'][:80]}")
        out.append("")

    # ========================================
    # SECTION 6: SUMMARY
    # ========================================
    out.append("=" * 80)
    out.append("SECTION 6: SUMMARY")
    out.append("=" * 80)
    out.append("")

    correct_all = sum(1 for d in valid if is_correct(d["verdict"], d["expected"]))
    correct_unseen = sum(1 for d in unseen if d.get("verdict") != "ERROR" and is_correct(d["verdict"], d["expected"]))
    valid_unseen = [d for d in unseen if d.get("verdict") != "ERROR"]

    out.append(f"  Pipeline verdict accuracy (all): {correct_all}/{len(valid)} ({100*correct_all/max(len(valid),1):.1f}%)")
    out.append(f"  Pipeline verdict accuracy (unseen only): {correct_unseen}/{len(valid_unseen)} ({100*correct_unseen/max(len(valid_unseen),1):.1f}%)")
    if total_sources > 0:
        out.append(f"  Per-source improvement over paragraph: {sent_only - para_only:+d} sources")
        out.append(f"  Paragraph per-source accuracy: {100*para_correct/total_sources:.1f}%")
        out.append(f"  Sentence (3K) per-source accuracy: {100*sent_correct/total_sources:.1f}%")
    out.append(f"  Myth-restating errors (fine-tuning target): {len(myth_restating)}")
    out.append(f"  Weak negation candidates (fine-tuning target): {len(weak_negation_candidates)}")
    out.append(f"  No-signal sources: {len(no_signal_sources)}")

    # Write
    os.makedirs("tests", exist_ok=True)
    with open(REPORT_PATH, "w") as f:
        f.write("\n".join(out))
    print(f"\nReport written to {REPORT_PATH}")
    print(f"\nQuick summary:")
    print(f"  Verdict accuracy (all): {correct_all}/{len(valid)}")
    print(f"  Verdict accuracy (unseen): {correct_unseen}/{len(valid_unseen)}")
    if total_sources > 0:
        print(f"  Per-source: paragraph {100*para_correct/total_sources:.1f}% -> sentence {100*sent_correct/total_sources:.1f}%")
    print(f"  Myth-restating errors: {len(myth_restating)}")
    print(f"  Weak negation candidates: {len(weak_negation_candidates)}")


# ============================================================
# MAIN
# ============================================================

def main():
    parser = argparse.ArgumentParser(description="Phase 2 Validation")
    parser.add_argument("--collect", action="store_true")
    parser.add_argument("--analyze", action="store_true")
    parser.add_argument("--both", action="store_true")
    args = parser.parse_args()

    if not (args.collect or args.analyze or args.both):
        print("Usage:")
        print("  python validation_setb.py --collect    # Run pipeline (~30-60 min)")
        print("  python validation_setb.py --analyze    # Analyze results (instant)")
        print("  python validation_setb.py --both")
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