"""
Decision 1 Test: Splitter Comparison on Real Enriched Content

Compares nltk sent_tokenize vs spaCy neural (en_core_web_sm) on actual
enriched pipeline output. This is the test that determines which splitter
we use for all subsequent work.

SETUP:
  pip install spacy --break-system-packages
  python -m spacy download en_core_web_sm

Uses Set A (20 diverse claims) for development/testing.
Set B (Phase 1 baseline 36 claims) is held back for final validation.

Usage: python decision1_splitter_test.py
Output: tests/decision1_splitter_report.txt
"""

import asyncio
import os
from datetime import datetime

import nltk
nltk.download('punkt_tab', quiet=True)
from nltk.tokenize import sent_tokenize

import spacy

# Load spaCy neural model (NOT the rule-based sentencizer)
# This uses dependency parsing for sentence boundaries
try:
    nlp_spacy = spacy.load("en_core_web_sm")
    print("Loaded spaCy en_core_web_sm (neural sentence segmentation)")
except OSError:
    print("ERROR: en_core_web_sm not found. Install with:")
    print("  python -m spacy download en_core_web_sm")
    print("Falling back to rule-based sentencizer (inferior, not recommended)")
    nlp_spacy = spacy.blank("en")
    nlp_spacy.add_pipe("sentencizer")


def split_nltk(text: str) -> list[str]:
    return sent_tokenize(text)


def split_spacy(text: str) -> list[str]:
    # spaCy has a default max length limit; increase for long snippets
    nlp_spacy.max_length = max(len(text) + 1000, nlp_spacy.max_length)
    doc = nlp_spacy(text)
    return [s.text.strip() for s in doc.sents if s.text.strip()]


# ============================================================
# SET A: Development claims (20 diverse claims)
# ============================================================
# Mix of: myths to debunk, supported facts, opinion claims,
# statistical claims, historical claims, current events.
# This diversity ensures splitter comparison covers different
# writing styles (fact-check articles, Wikipedia, academic, news).

SET_A_CLAIMS = [
    # Myths/misconceptions (expect opposing from debunking sources)
    "vaccines cause autism",
    "the earth is flat",
    "humans only use 10 percent of their brain",
    "cracking your knuckles causes arthritis",
    "sugar makes children hyperactive",
    "the great wall of china is visible from space",
    "lightning never strikes the same place twice",
    "lemmings commit mass suicide",
    # Supported scientific facts (expect supporting)
    "climate change is caused by human activity",
    "smoking causes lung cancer",
    "the earth revolves around the sun",
    # False claims to debunk (expect opposing)
    "the moon landing was faked",
    "5G towers cause cancer",
    "drinking bleach cures diseases",
    # Nuanced/contested claims (mixed signals expected)
    "nuclear energy is safe",
    "organic food is healthier than conventional food",
    "video games cause violence",
    # Historical claims
    "christopher columbus discovered america",
    # Statistical/specific claims
    "the average human body temperature is 98.6 degrees fahrenheit",
    "goldfish have a three second memory",
]


# ============================================================
# PIPELINE INTEGRATION
# ============================================================

async def fetch_enriched_sources(claim_text: str) -> list[dict]:
    """Run a claim through the pipeline's source fetching and enrichment."""
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
        if len(snippet.split()) >= 30:  # only enriched sources
            results.append({
                "title": source.title or "",
                "snippet": snippet,
                "source_type": source.source_type or "",
                "word_count": len(snippet.split()),
            })
    return results


# ============================================================
# COMPARISON LOGIC
# ============================================================

def compare_splits(text: str) -> dict:
    """Compare nltk vs spaCy splits on a single text.
    Returns detailed comparison."""
    nltk_sents = split_nltk(text)
    spacy_sents = split_spacy(text)

    # Check if they produce the same number of sentences
    count_match = len(nltk_sents) == len(spacy_sents)

    # Check if texts match (even if counts match, boundaries could differ)
    text_match = count_match and all(
        n.strip() == s.strip()
        for n, s in zip(nltk_sents, spacy_sents)
    )

    # Find specific differences
    differences = []
    if not text_match:
        # Align sentences to find where they diverge
        # Simple approach: find first divergence point
        max_len = max(len(nltk_sents), len(spacy_sents))
        for i in range(max_len):
            n = nltk_sents[i].strip() if i < len(nltk_sents) else "<MISSING>"
            s = spacy_sents[i].strip() if i < len(spacy_sents) else "<MISSING>"
            if n != s:
                differences.append({
                    "index": i,
                    "nltk": n[:200],
                    "spacy": s[:200],
                })
                # After first difference, alignment may be off
                # Just record count difference from here
                if len(differences) >= 5:
                    break

    return {
        "nltk_count": len(nltk_sents),
        "spacy_count": len(spacy_sents),
        "count_match": count_match,
        "text_match": text_match,
        "differences": differences,
        "nltk_sents": nltk_sents,
        "spacy_sents": spacy_sents,
    }


def categorize_difference(diff: dict) -> str:
    """Categorize what kind of splitting difference occurred."""
    nltk_text = diff.get("nltk", "")
    spacy_text = diff.get("spacy", "")

    # Check for common patterns
    if "<MISSING>" in nltk_text or "<MISSING>" in spacy_text:
        return "count_mismatch"

    # Check if one merged what the other split
    if len(nltk_text) > len(spacy_text) * 1.5:
        return "spacy_split_more"
    elif len(spacy_text) > len(nltk_text) * 1.5:
        return "nltk_split_more"

    # Check for abbreviation handling
    abbrev_patterns = ["Dr.", "Mr.", "Mrs.", "Jr.", "Sr.", "vs.", "etc.",
                       "i.e.", "e.g.", "U.S.", "U.K.", "Vol.", "No.",
                       "Fig.", "Ref.", "pp.", "ed.", "al."]
    for abbrev in abbrev_patterns:
        if abbrev in nltk_text or abbrev in spacy_text:
            return "abbreviation_handling"

    # Check for number/decimal handling
    import re
    if re.search(r'\d+\.\d+', nltk_text) or re.search(r'\d+\.\d+', spacy_text):
        return "decimal_number"

    return "boundary_shift"


# ============================================================
# MAIN
# ============================================================

async def main():
    out = []
    out.append(f"Decision 1: Splitter Comparison (nltk vs spaCy neural)")
    out.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    out.append(f"Claims: {len(SET_A_CLAIMS)} (Set A)")
    out.append(f"nltk: sent_tokenize (Punkt)")
    out.append(f"spaCy: en_core_web_sm (neural dependency parser)")
    out.append("")
    out.append("=" * 100)

    # Stats
    total_sources = 0
    total_agree = 0
    total_disagree = 0
    category_counts = {}
    disagree_details = []

    for ci, claim in enumerate(SET_A_CLAIMS):
        out.append(f"")
        out.append(f"CLAIM {ci+1}/{len(SET_A_CLAIMS)}: \"{claim}\"")
        out.append(f"-" * 80)

        print(f"Processing claim {ci+1}/{len(SET_A_CLAIMS)}: {claim}")

        try:
            sources = await fetch_enriched_sources(claim)
        except Exception as e:
            out.append(f"  ERROR: {e}")
            continue

        out.append(f"  Enriched sources: {len(sources)}")

        for si, source in enumerate(sources):
            total_sources += 1
            comp = compare_splits(source["snippet"])

            if comp["text_match"]:
                total_agree += 1
                # Don't clutter output with agreements
                continue

            total_disagree += 1

            out.append(f"")
            out.append(f"  Source {si+1}: {source['title'][:70]}")
            out.append(f"  [{source['word_count']}w, nltk={comp['nltk_count']} sents, spacy={comp['spacy_count']} sents]")
            out.append(f"  ** DISAGREE **")

            for di, diff in enumerate(comp["differences"]):
                cat = categorize_difference(diff)
                category_counts[cat] = category_counts.get(cat, 0) + 1

                out.append(f"")
                out.append(f"    Difference {di+1} (at index {diff['index']}, type: {cat}):")
                out.append(f"    nltk:  \"{diff['nltk']}\"")
                out.append(f"    spacy: \"{diff['spacy']}\"")

            # Store for summary
            disagree_details.append({
                "claim": claim,
                "source": source["title"][:60],
                "nltk_count": comp["nltk_count"],
                "spacy_count": comp["spacy_count"],
                "num_differences": len(comp["differences"]),
                "categories": [categorize_difference(d) for d in comp["differences"]],
            })

        # Show claim-level agreement rate
        claim_sources = len(sources)
        claim_disagree = sum(1 for d in disagree_details if d["claim"] == claim)
        claim_agree = claim_sources - claim_disagree
        out.append(f"  Claim summary: {claim_agree}/{claim_sources} agree, {claim_disagree}/{claim_sources} disagree")

    # ============================================================
    # SUMMARY
    # ============================================================
    out.append("")
    out.append("=" * 100)
    out.append("SUMMARY")
    out.append("=" * 100)
    out.append(f"Total enriched sources compared: {total_sources}")
    out.append(f"Splitters AGREE (identical output): {total_agree} ({100*total_agree/max(total_sources,1):.1f}%)")
    out.append(f"Splitters DISAGREE: {total_disagree} ({100*total_disagree/max(total_sources,1):.1f}%)")
    out.append("")

    if category_counts:
        out.append("Difference categories:")
        for cat, count in sorted(category_counts.items(), key=lambda x: -x[1]):
            out.append(f"  {cat:30s}: {count}")
    out.append("")

    # Count difference magnitude
    if disagree_details:
        count_diffs = [abs(d["nltk_count"] - d["spacy_count"]) for d in disagree_details]
        out.append(f"When they disagree, sentence count difference:")
        out.append(f"  Mean: {sum(count_diffs)/len(count_diffs):.1f}")
        out.append(f"  Max:  {max(count_diffs)}")
        out.append(f"  Sources with count diff > 3: {sum(1 for d in count_diffs if d > 3)}")
    out.append("")

    out.append("INTERPRETATION:")
    out.append("  If agreement > 95%: splitter choice doesn't matter, pick either.")
    out.append("  If agreement 80-95%: look at disagreement categories.")
    out.append("    - abbreviation_handling: nltk likely better (trained on abbreviations)")
    out.append("    - boundary_shift: check which produces more meaningful NLI-ready sentences")
    out.append("    - decimal_number: check which handles 'Fig. 3' or '0.05%' correctly")
    out.append("  If agreement < 80%: significant difference, need NLI accuracy comparison.")

    # Write
    os.makedirs("tests", exist_ok=True)
    path = "tests/decision1_splitter_report.txt"
    with open(path, "w") as f:
        f.write("\n".join(out))
    print(f"\nReport written to {path}")
    print(f"Total sources: {total_sources}")
    print(f"Agree: {total_agree} ({100*total_agree/max(total_sources,1):.1f}%)")
    print(f"Disagree: {total_disagree} ({100*total_disagree/max(total_sources,1):.1f}%)")
    if category_counts:
        print(f"Top category: {max(category_counts, key=category_counts.get)}")


if __name__ == "__main__":
    asyncio.run(main())