"""
Step 1: Collect source-claim pairs from the actual pipeline.

Run this from your project root:
    python -m training.collect_training_data

It will:
1. Run each claim through search_sources() to get real sources
2. Run NLI on each source-claim pair to get the CURRENT model's prediction
3. Save everything to a CSV for manual labeling
4. You review each row and fill in the 'correct_label' column

The 'current_nli_label' column shows what the model currently predicts.
For most rows, the model is right and you just confirm.
Focus your attention on rows where confidence is low (0.4-0.7) or
where the pattern column flags a potential issue.
"""
import asyncio
import csv
import sys
import os
import re

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.models.schemas import ClaimRequest
from app.services.claim_service import search_sources, _deduplicate_sources, _filter_relevant_sources
from app.services.nli_service import classify_stance


# 40 claims deliberately chosen to NOT overlap with the 36-claim test set.
# Covers myths, contested topics, factual claims, and opinion-style claims.
# Selected to naturally trigger the patterns we identified.
TRAINING_CLAIMS = [
    # Myths / misconceptions (should trigger reporting frame patterns)
    "cracking your knuckles causes arthritis",
    "lightning never strikes the same place twice",
    "humans swallow spiders in their sleep",
    "shaving makes hair grow back thicker",
    "the tongue has different taste zones",
    "Napoleon was short",
    "you need to wait 24 hours to file a missing person report",
    "bats are blind",
    "Vikings wore horned helmets",
    "lemmings jump off cliffs",

    # Contested / debatable (should produce mixed sources)
    "homework improves student performance",
    "the death penalty deters crime",
    "minimum wage increases cause unemployment",
    "meditation has proven health benefits",
    "bilingual children develop language skills slower",
    "red wine is good for heart health",
    "free trade benefits all countries equally",
    "spanking children is an effective form of discipline",
    "breakfast is the most important meal of the day",
    "video surveillance reduces crime rates",

    # Factual claims (should be clearly supported or opposed)
    "the sun is a star",
    "diamonds are made of carbon",
    "the Sahara is the largest desert in the world",
    "Mount Everest is the tallest mountain on Earth",
    "octopuses have three hearts",
    "bananas are berries",
    "the human body has 206 bones",
    "sound cannot travel through a vacuum",
    "glass is a liquid that flows very slowly",
    "the Amazon River is the longest river in the world",

    # Opinion / value claims (should trigger opinion-like patterns)
    "classical music is better than pop music",
    "cities are better places to live than rural areas",
    "the internet has done more harm than good",
    "professional athletes are overpaid",
    "zoos are unethical",
    "space exploration is a waste of money",
    "electric cars are better than gasoline cars",
    "working from home should be a permanent option",
    "standardized testing should be abolished",
    "the drinking age should be lowered to 18",
]


def _detect_potential_pattern(source_text: str, nli_label: str, nli_conf: float) -> str:
    """Flag sources that might be misclassified due to known patterns."""
    text_lower = source_text.lower()
    flags = []

    # Pattern 1: Reporting frames
    reporting_cues = [
        "the notion that", "the belief that", "the myth that",
        "the misconception that", "the idea that", "widely believed",
        "commonly thought", "popular belief", "often claimed",
        "conspiracy theories claim", "proponents argue",
        "it is said that", "legend has it", "the claim that",
        "pseudoscience", "old wives' tale", "urban legend",
    ]
    if any(cue in text_lower for cue in reporting_cues):
        if nli_label == "supporting" and nli_conf > 0.5:
            flags.append("REPORTING_FRAME?")

    # Pattern 2: Keyword association (academic text about topic)
    academic_cues = [
        "this study", "this paper", "our research", "we investigate",
        "we examine", "abstract", "findings suggest", "results indicate",
        "participants", "methodology",
    ]
    if any(cue in text_lower for cue in academic_cues):
        if nli_label != "neutral":
            flags.append("ACADEMIC_MAYBE_NEUTRAL?")

    # Pattern 4: Weak negation
    weak_neg_cues = [
        "failed to find", "unable to", "don't think",
        "remains inconclusive", "no convincing evidence",
        "has not been established", "does not support",
        "little evidence", "insufficient evidence",
    ]
    if any(cue in text_lower for cue in weak_neg_cues):
        if nli_label != "opposing":
            flags.append("WEAK_NEGATION?")

    # Pattern 3: Sentiment vs stance (negative framing of agreement)
    negative_agreement_cues = [
        "devastating", "alarming", "catastroph", "crisis",
        "unfortunately", "tragically", "at the cost of",
    ]
    if any(cue in text_lower for cue in negative_agreement_cues):
        if nli_label == "opposing":
            flags.append("SENTIMENT_NOT_STANCE?")

    return " | ".join(flags) if flags else ""


async def collect_for_claim(claim: str) -> list[dict]:
    """Run a single claim through the pipeline and collect source-NLI pairs."""
    request = ClaimRequest(claim=claim)

    # Get sources from all APIs
    raw_sources = await search_sources(request)
    raw_sources = _filter_relevant_sources(claim, raw_sources)
    raw_sources = _deduplicate_sources(raw_sources)

    rows = []
    for source in raw_sources:
        if not source.snippet:
            continue

        # Skip wikidata (excluded from NLI in the pipeline)
        if source.source_type == "knowledge_graph":
            continue

        # Skip fact-check sources (handled by rating bypass at inference,
        # NLI never classifies these - their snippet is just the false claim
        # text, not the article content, so training on them would be harmful)
        if source.source_type == "fact_check":
            continue

        # Skip academic sources with no abstract (title-only fallback,
        # too short for meaningful NLI classification)
        if source.source_type == "academic":
            title = (source.title or "").strip()
            snippet_text = (source.snippet or "").strip()
            if snippet_text == title or len(snippet_text.split()) < 20:
                continue

        snippet = source.snippet
        source_type = source.source_type or "web"

        # Truncate very long snippets to match inference behavior
        # (tokenizer truncates at 512 tokens anyway)
        snippet_words = snippet.split()
        if len(snippet_words) > 300:
            snippet = " ".join(snippet_words[:300]) + "..."

        # Get current model's prediction
        nli_label, nli_conf = classify_stance(snippet, claim)

        # Detect potential pattern issues
        pattern_flag = _detect_potential_pattern(snippet, nli_label, nli_conf)

        rows.append({
            "claim": claim,
            "source_text": snippet,
            "source_type": source_type,
            "title": source.title[:100] if source.title else "",
            "url": source.url[:150] if source.url else "",
            "current_nli_label": nli_label,
            "current_nli_confidence": round(nli_conf, 3),
            "pattern_flag": pattern_flag,
            "correct_label": "",  # YOU FILL THIS IN
            # Label guide: 0 = supporting, 1 = neutral, 2 = opposing
        })

    return rows


async def main():
    output_path = "training/api_sourced_pairs.csv"
    os.makedirs("training", exist_ok=True)

    all_rows = []
    total_claims = len(TRAINING_CLAIMS)

    for i, claim in enumerate(TRAINING_CLAIMS):
        print(f"\n[{i+1}/{total_claims}] Collecting: \"{claim}\"")
        try:
            rows = await collect_for_claim(claim)
            all_rows.extend(rows)
            print(f"  -> {len(rows)} source-claim pairs collected")
        except Exception as e:
            print(f"  -> ERROR: {e}")

    # Write to CSV
    fieldnames = [
        "claim", "source_text", "source_type", "title", "url",
        "current_nli_label", "current_nli_confidence",
        "pattern_flag", "correct_label",
    ]
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_rows)

    # Summary
    print(f"\n{'='*60}")
    print(f"COLLECTION COMPLETE")
    print(f"{'='*60}")
    print(f"Total source-claim pairs: {len(all_rows)}")
    print(f"Saved to: {output_path}")

    # Stats
    from collections import Counter
    label_dist = Counter(r["current_nli_label"] for r in all_rows)
    flagged = sum(1 for r in all_rows if r["pattern_flag"])
    print(f"\nCurrent model predictions:")
    for label, count in label_dist.most_common():
        print(f"  {label}: {count}")
    print(f"\nFlagged for review: {flagged} pairs")
    print(f"  (these are sources where the model might be wrong)")

    print(f"\n--- LABELING INSTRUCTIONS ---")
    print(f"1. Open {output_path} in a spreadsheet editor")
    print(f"2. For each row, fill in the 'correct_label' column:")
    print(f"   0 = source SUPPORTS the claim")
    print(f"   1 = source is NEUTRAL (discusses topic without taking a stance)")
    print(f"   2 = source OPPOSES the claim")
    print(f"3. Start with flagged rows (pattern_flag column)")
    print(f"4. For unflagged rows, the current_nli_label is usually correct")
    print(f"   Just verify and copy the numeric label:")
    print(f"   supporting -> 0, neutral -> 1, opposing -> 2")
    print(f"5. Save the file when done")


if __name__ == "__main__":
    asyncio.run(main())