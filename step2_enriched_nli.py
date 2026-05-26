"""
Phase 2 Step 2: Sentence-Level NLI on Real Enriched Snippets

PURPOSE: Test whether sentence-level NLI helps on actual 100-400 word
enriched snippets from content_extractor. Step 1 showed sentence-level
NLI HURTS on short synthetic test samples. But the enrichment regression
(-6.8pp from Phase 1) is about LONG enriched text pushing the model
toward neutral. Sentence splitting might recover that.

HOW IT WORKS:
  1. Runs 10 claims through the full pipeline (source fetch + enrichment)
  2. For each enriched source (>3 sentences), compares:
     - Paragraph-level NLI (full enriched snippet)
     - Per-sentence NLI (each sentence independently)
  3. Shows full probability distributions for everything

WHAT TO LOOK FOR:
  - Do long enriched snippets produce more neutral results than they should?
  - Do individual sentences within those snippets carry clearer signal?
  - Does the myth>debunk confidence pattern from Step 1 persist with
    real content, or was that specific to the synthetic test set?

REQUIRES: Full project with API keys configured, model loaded.

Usage: python step2_enriched_nli.py
Output: tests/step2_enriched_output.txt
"""

import asyncio
import os
import sys
from datetime import datetime

import nltk
nltk.download('punkt_tab', quiet=True)
from nltk.tokenize import sent_tokenize

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# ============================================================
# MODEL
# ============================================================
MODEL_NAME = "MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli"
print(f"Loading {MODEL_NAME}...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
model.eval()
print("Model loaded.\n")

LABEL_MAP = {0: "supporting", 1: "neutral", 2: "opposing"}


def nli_batch(premises: list[str], hypotheses: list[str]) -> list[dict]:
    """Batched NLI inference. Returns list of {label, conf, p_supp, p_neut, p_opp}."""
    if not premises:
        return []
    inputs = tokenizer(
        premises, hypotheses,
        return_tensors="pt", truncation=True, padding=True, max_length=512,
    )
    with torch.no_grad():
        outputs = model(**inputs)
    all_probs = torch.softmax(outputs.logits, dim=1)
    results = []
    for probs in all_probs:
        p = probs.tolist()
        idx = probs.argmax().item()
        results.append({
            "label": LABEL_MAP[idx],
            "conf": round(p[idx], 4),
            "p_supp": round(p[0], 4),
            "p_neut": round(p[1], 4),
            "p_opp": round(p[2], 4),
        })
    return results


# ============================================================
# TEST CLAIMS
# ============================================================
# Mix of claims that should produce different verdicts and source types.
# Chosen to cover: scientific myths, political claims, factual claims,
# and opinion claims.
TEST_CLAIMS = [
    # Claims where NLI accuracy has been problematic
    "vaccines cause autism",
    "the earth is flat",
    "humans only use 10 percent of their brain",
    "the great wall of china is visible from space",
    "cracking your knuckles causes arthritis",
    "sugar makes children hyperactive",
    "lemmings commit mass suicide",
    "lightning never strikes the same place twice",
    # Factual claims that should be clearly supported/opposed
    "climate change is caused by human activity",
    "the moon landing was faked",
]


# ============================================================
# PIPELINE INTEGRATION
# ============================================================

async def fetch_enriched_sources(claim_text: str) -> list[dict]:
    """Run a claim through the pipeline's source fetching and enrichment.
    Returns list of {title, url, snippet, source_type, word_count, metadata}."""
    from app.models.schemas import ClaimRequest
    from app.services.claim_service import search_sources, _filter_relevant_sources, _deduplicate_sources
    from app.services.claim_classifier import classify_claim_domain
    from app.services.source_router import build_routing_config

    request = ClaimRequest(claim=claim_text)
    domain = classify_claim_domain(claim_text)
    routing = build_routing_config(domain, claim_text)

    raw = await search_sources(request, routing)
    raw = _filter_relevant_sources(claim_text, raw)
    raw = _deduplicate_sources(raw)

    results = []
    for source in raw:
        snippet = source.snippet or ""
        results.append({
            "title": source.title or "",
            "url": source.url or "",
            "snippet": snippet,
            "source_type": source.source_type or "",
            "word_count": len(snippet.split()),
            "metadata": source.metadata or {},
        })
    return results


# ============================================================
# ANALYSIS
# ============================================================

def analyze_snippet(claim: str, snippet: str, title: str) -> dict:
    """Run paragraph-level and sentence-level NLI on an enriched snippet.
    Returns full detail for output."""

    # Paragraph-level
    para_result = nli_batch([snippet], [claim])[0]

    # Sentence-level
    sentences = sent_tokenize(snippet)
    sent_results = []
    if sentences:
        nli_results = nli_batch(sentences, [claim] * len(sentences))
        for sent, nli_r in zip(sentences, nli_results):
            sent_results.append({
                "text": sent,
                "word_count": len(sent.split()),
                **nli_r,
            })

    return {
        "title": title,
        "snippet_words": len(snippet.split()),
        "num_sentences": len(sentences),
        "paragraph": para_result,
        "sentences": sent_results,
    }


def format_analysis(claim: str, source_idx: int, analysis: dict) -> list[str]:
    """Format a single source analysis for output."""
    lines = []
    p = analysis["paragraph"]
    lines.append(f"  Source {source_idx}: {analysis['title'][:80]}")
    lines.append(f"  [{analysis['snippet_words']}w, {analysis['num_sentences']} sentences]")
    lines.append(f"  PARA: {p['label']:10s} [S:{p['p_supp']:.4f} N:{p['p_neut']:.4f} O:{p['p_opp']:.4f}] conf={p['conf']:.4f}")
    lines.append("")

    for j, sr in enumerate(analysis["sentences"]):
        lines.append(
            f"  S{j+1:2d}: {sr['label']:10s} "
            f"[S:{sr['p_supp']:.4f} N:{sr['p_neut']:.4f} O:{sr['p_opp']:.4f}] "
            f"conf={sr['conf']:.4f}  [{sr['word_count']}w]"
        )
        # Show sentence text, truncated for readability but enough to understand
        text_preview = sr['text'][:150]
        if len(sr['text']) > 150:
            text_preview += "..."
        lines.append(f"        \"{text_preview}\"")

    # Summary comparison
    lines.append("")
    non_neutral_sents = [sr for sr in analysis["sentences"] if sr["label"] != "neutral"]
    if non_neutral_sents:
        max_supp_sent = max(analysis["sentences"], key=lambda x: x["p_supp"])
        max_opp_sent = max(analysis["sentences"], key=lambda x: x["p_opp"])
        lines.append(f"  Max P(supp) sentence: {max_supp_sent['p_supp']:.4f} (S{analysis['sentences'].index(max_supp_sent)+1})")
        lines.append(f"  Max P(opp)  sentence: {max_opp_sent['p_opp']:.4f} (S{analysis['sentences'].index(max_opp_sent)+1})")

        # Compare paragraph vs best sentence signal
        para_dominant = "supporting" if p["p_supp"] > p["p_opp"] else "opposing"
        para_signal = max(p["p_supp"], p["p_opp"])
        sent_dominant = "supporting" if max_supp_sent["p_supp"] > max_opp_sent["p_opp"] else "opposing"
        sent_signal = max(max_supp_sent["p_supp"], max_opp_sent["p_opp"])

        if para_dominant != sent_dominant:
            lines.append(f"  ** PARA vs SENT DISAGREE: para={para_dominant}({para_signal:.4f}) sent={sent_dominant}({sent_signal:.4f}) **")
        elif sent_signal > para_signal:
            lines.append(f"  Sentence signal STRONGER: {sent_signal:.4f} vs para {para_signal:.4f} (+{sent_signal-para_signal:.4f})")
        else:
            lines.append(f"  Paragraph signal stronger: {para_signal:.4f} vs sent {sent_signal:.4f}")
    else:
        lines.append(f"  All sentences neutral. Para: {p['label']} ({p['conf']:.4f})")
        if p["label"] != "neutral":
            lines.append(f"  ** REGRESSION: paragraph non-neutral but all sentences neutral **")

    lines.append("")
    return lines


# ============================================================
# MAIN
# ============================================================

async def main():
    out = []
    out.append(f"Phase 2 Step 2: Sentence-Level NLI on Real Enriched Snippets")
    out.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    out.append(f"Model: {MODEL_NAME}")
    out.append(f"Splitter: nltk sent_tokenize")
    out.append(f"Claims: {len(TEST_CLAIMS)}")
    out.append(f"")
    out.append(f"Only showing sources with >3 sentences (enriched content)")
    out.append(f"Short snippet sources (1-3 sentences) behave same as Step 1")
    out.append("=" * 100)

    # Counters
    total_sources_analyzed = 0
    para_stronger_count = 0
    sent_stronger_count = 0
    disagree_count = 0
    all_neutral_regression = 0

    for claim_idx, claim in enumerate(TEST_CLAIMS):
        out.append(f"")
        out.append(f"{'='*100}")
        out.append(f"CLAIM {claim_idx+1}/{len(TEST_CLAIMS)}: \"{claim}\"")
        out.append(f"{'='*100}")
        out.append(f"")

        print(f"Processing claim {claim_idx+1}/{len(TEST_CLAIMS)}: {claim}")

        try:
            sources = await fetch_enriched_sources(claim)
        except Exception as e:
            out.append(f"  ERROR fetching sources: {e}")
            continue

        out.append(f"  Total sources: {len(sources)}")

        # Filter to enriched sources with enough sentences to matter
        enriched = [s for s in sources if s["word_count"] >= 30]
        out.append(f"  Sources with 30+ words: {len(enriched)}")

        multi_sentence = []
        for s in enriched:
            sents = sent_tokenize(s["snippet"])
            if len(sents) > 3:
                multi_sentence.append(s)

        out.append(f"  Sources with >3 sentences: {len(multi_sentence)}")
        out.append(f"")

        if not multi_sentence:
            out.append(f"  No multi-sentence enriched sources for this claim.")
            # Still show a few short sources for comparison
            for si, s in enumerate(enriched[:3]):
                analysis = analyze_snippet(claim, s["snippet"], s["title"])
                out.extend(format_analysis(claim, si+1, analysis))
            continue

        for si, s in enumerate(multi_sentence):
            analysis = analyze_snippet(claim, s["snippet"], s["title"])
            out.extend(format_analysis(claim, si+1, analysis))
            total_sources_analyzed += 1

            # Track stats
            p = analysis["paragraph"]
            sents = analysis["sentences"]
            non_neutral = [sr for sr in sents if sr["label"] != "neutral"]

            if not non_neutral and p["label"] != "neutral":
                all_neutral_regression += 1

            if sents:
                max_supp_s = max(sr["p_supp"] for sr in sents)
                max_opp_s = max(sr["p_opp"] for sr in sents)
                sent_signal = max(max_supp_s, max_opp_s)
                para_signal = max(p["p_supp"], p["p_opp"])

                sent_dominant = "supporting" if max_supp_s > max_opp_s else "opposing"
                para_dominant = "supporting" if p["p_supp"] > p["p_opp"] else "opposing"

                if para_dominant != sent_dominant:
                    disagree_count += 1
                elif sent_signal > para_signal:
                    sent_stronger_count += 1
                else:
                    para_stronger_count += 1

        out.append("-" * 100)

    # Summary
    out.append("")
    out.append("=" * 100)
    out.append("SUMMARY")
    out.append("=" * 100)
    out.append(f"Total multi-sentence sources analyzed: {total_sources_analyzed}")
    out.append(f"Paragraph signal stronger: {para_stronger_count}")
    out.append(f"Sentence signal stronger: {sent_stronger_count}")
    out.append(f"Para vs Sent disagree on direction: {disagree_count}")
    out.append(f"All-sentences-neutral regression: {all_neutral_regression}")
    out.append(f"")
    out.append("INTERPRETATION:")
    out.append("  If 'Sentence signal stronger' >> 'Paragraph signal stronger':")
    out.append("    Sentence-level NLI helps on enriched content.")
    out.append("  If 'Paragraph signal stronger' dominates:")
    out.append("    Enriched snippets work better as whole paragraphs.")
    out.append("  If 'All-sentences-neutral regression' is high:")
    out.append("    Splitting destroys signal (same problem as Step 1).")

    # Write
    os.makedirs("tests", exist_ok=True)
    path = "tests/step2_enriched_output.txt"
    with open(path, "w") as f:
        f.write("\n".join(out))
    print(f"\nOutput written to {path}")
    print(f"Sources analyzed: {total_sources_analyzed}")
    print(f"Para stronger: {para_stronger_count} | Sent stronger: {sent_stronger_count} | Disagree: {disagree_count} | Regression: {all_neutral_regression}")


if __name__ == "__main__":
    asyncio.run(main())