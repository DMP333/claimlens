"""
Fresh Pipeline Collection: Run all 62 claims through current pipeline.
Captures per-source and per-sentence NLI data for comprehensive analysis.

Usage: python collect_fresh_baseline.py
Output: data/fresh_pipeline_results.json

Takes ~30-60 minutes depending on API response times.
Saves progress after each claim so you can resume if interrupted.
"""

import asyncio
import json
import time
import os
import sys
from pathlib import Path

# Adjust this import to match your project structure
# If your project uses `from app.services.X import Y`:
from app.models.schemas import ClaimRequest, Source
from app.services.claim_service import search_sources, _filter_relevant_sources, _deduplicate_sources, _stance_from_factcheck, RATING_LOOKUP
from app.services.nli_service import classify_stance_sentences, compute_relevance
from app.services.claim_classifier import classify_claim_type, classify_claim_domain
from app.services.source_router import build_routing_config
from app.services.credibility_service import score_all_sources


# ============================================================
# CLAIM LIST (62 claims with expected verdicts)
# ============================================================

CLAIMS = [
    {"claim": "5G causes COVID", "expected_verdict": "strongly opposed", "category": "factual_false"},
    {"claim": "5G towers cause cancer", "expected_verdict": "strongly opposed", "category": "factual_false"},
    {"claim": "AI will replace most jobs", "expected_verdict": "contested", "category": "contested"},
    {"claim": "China has the world's largest economy", "expected_verdict": "contested", "category": "current_event"},
    {"claim": "Einstein failed math in school", "expected_verdict": "strongly opposed", "category": "factual_false"},
    {"claim": "LeBron James is the greatest basketball player of all time", "expected_verdict": "opinion", "category": "opinion"},
    {"claim": "MSG is dangerous to consume", "expected_verdict": "strongly opposed", "category": "factual_false"},
    {"claim": "antibiotics do not work against viruses", "expected_verdict": "strongly supported", "category": "factual_true"},
    {"claim": "bats are blind", "expected_verdict": "strongly opposed", "category": "factual_false"},
    {"claim": "bulls are enraged by the color red", "expected_verdict": "strongly opposed", "category": "factual_false"},
    {"claim": "capitalism is better than socialism", "expected_verdict": "opinion", "category": "opinion"},
    {"claim": "cats are better pets than dogs", "expected_verdict": "opinion", "category": "opinion"},
    {"claim": "christopher columbus discovered america", "expected_verdict": "strongly opposed", "category": "factual_false"},
    {"claim": "climate change is caused by human activity", "expected_verdict": "strongly supported", "category": "factual_true"},
    {"claim": "climate change is real", "expected_verdict": "strongly supported", "category": "factual_true"},
    {"claim": "college education is worth the cost", "expected_verdict": "opinion", "category": "opinion"},
    {"claim": "cracking your knuckles causes arthritis", "expected_verdict": "strongly opposed", "category": "factual_false"},
    {"claim": "cryptocurrency is a good long-term investment", "expected_verdict": "opinion", "category": "opinion"},
    {"claim": "democracy is the best form of government", "expected_verdict": "opinion", "category": "opinion"},
    {"claim": "dogs can only see in black and white", "expected_verdict": "strongly opposed", "category": "factual_false"},
    {"claim": "drinking bleach cures diseases", "expected_verdict": "strongly opposed", "category": "factual_false"},
    {"claim": "eating carrots improves your eyesight", "expected_verdict": "strongly opposed", "category": "factual_false"},
    {"claim": "evolution is real", "expected_verdict": "strongly supported", "category": "factual_true"},
    {"claim": "goldfish have a 3 second memory", "expected_verdict": "strongly opposed", "category": "factual_false"},
    {"claim": "goldfish have a three second memory", "expected_verdict": "strongly opposed", "category": "factual_false"},
    {"claim": "honey never expires", "expected_verdict": "strongly supported", "category": "factual_true"},
    {"claim": "humans only use 10 percent of their brain", "expected_verdict": "strongly opposed", "category": "factual_false"},
    {"claim": "humans share about 98% of DNA with chimpanzees", "expected_verdict": "strongly supported", "category": "factual_true"},
    {"claim": "immigration is good for the economy", "expected_verdict": "contested", "category": "contested"},
    {"claim": "inflation in the United States is under control", "expected_verdict": "contested", "category": "current_event"},
    {"claim": "lemmings commit mass suicide", "expected_verdict": "strongly opposed", "category": "factual_false"},
    {"claim": "lightning never strikes the same place twice", "expected_verdict": "strongly opposed", "category": "factual_false"},
    {"claim": "nuclear energy is safe", "expected_verdict": "contested", "category": "contested"},
    {"claim": "octopuses have three hearts", "expected_verdict": "strongly supported", "category": "factual_true"},
    {"claim": "organic food is healthier than conventional food", "expected_verdict": "contested", "category": "contested"},
    {"claim": "pineapple belongs on pizza", "expected_verdict": "opinion", "category": "opinion"},
    {"claim": "remote work is more productive than office work", "expected_verdict": "contested", "category": "contested"},
    {"claim": "shaving makes hair grow back thicker", "expected_verdict": "strongly opposed", "category": "factual_false"},
    {"claim": "smoking causes lung cancer", "expected_verdict": "strongly supported", "category": "factual_true"},
    {"claim": "social media is harmful to mental health", "expected_verdict": "contested", "category": "contested"},
    {"claim": "sugar is worse than fat for health", "expected_verdict": "contested", "category": "contested"},
    {"claim": "sugar makes children hyperactive", "expected_verdict": "strongly opposed", "category": "factual_false"},
    {"claim": "the Amazon rainforest produces about 20% of the world's oxygen", "expected_verdict": "strongly opposed", "category": "factual_false"},
    {"claim": "the Beatles are the greatest band of all time", "expected_verdict": "opinion", "category": "opinion"},
    {"claim": "the Great Wall of China is the only man-made structure visible from space", "expected_verdict": "strongly opposed", "category": "factual_false"},
    {"claim": "the Great Wall of China is visible from space", "expected_verdict": "strongly opposed", "category": "factual_false"},
    {"claim": "the Sahara desert is the largest desert on earth", "expected_verdict": "strongly opposed", "category": "factual_false"},
    {"claim": "the United States economy is in a recession", "expected_verdict": "contested", "category": "current_event"},
    {"claim": "the average human body temperature is 98.6 degrees fahrenheit", "expected_verdict": "strongly opposed", "category": "factual_false"},
    {"claim": "the earth is flat", "expected_verdict": "strongly opposed", "category": "factual_false"},
    {"claim": "the earth revolves around the sun", "expected_verdict": "strongly supported", "category": "factual_true"},
    {"claim": "the great wall of china is visible from space", "expected_verdict": "strongly opposed", "category": "factual_false"},
    {"claim": "the moon landing was faked", "expected_verdict": "strongly opposed", "category": "factual_false"},
    {"claim": "the speed of light is constant", "expected_verdict": "strongly supported", "category": "factual_true"},
    {"claim": "the sun is a star", "expected_verdict": "strongly supported", "category": "factual_true"},
    {"claim": "universal basic income reduces poverty", "expected_verdict": "contested", "category": "contested"},
    {"claim": "vaccines cause autism", "expected_verdict": "strongly opposed", "category": "factual_false"},
    {"claim": "video games cause violence", "expected_verdict": "contested", "category": "contested"},
    {"claim": "violent video games cause real world violence", "expected_verdict": "contested", "category": "contested"},
    {"claim": "water boils at 100 degrees celsius", "expected_verdict": "strongly supported", "category": "factual_true"},
    {"claim": "we only use 10% of our brains", "expected_verdict": "strongly opposed", "category": "factual_false"},
    {"claim": "you lose most body heat through your head", "expected_verdict": "strongly opposed", "category": "factual_false"},
]


# ============================================================
# COLLECTION LOGIC
# ============================================================

OUTPUT_DIR = Path("data")
OUTPUT_DIR.mkdir(exist_ok=True)
RESULTS_FILE = OUTPUT_DIR / "fresh_pipeline_results.json"
PROGRESS_FILE = OUTPUT_DIR / "collection_progress.json"


def load_progress():
    """Load previously collected results for resume capability."""
    if PROGRESS_FILE.exists():
        with open(PROGRESS_FILE) as f:
            return json.load(f)
    return {}


def save_progress(results):
    """Save progress after each claim."""
    with open(PROGRESS_FILE, 'w') as f:
        json.dump(results, f, indent=2)


async def collect_claim(claim_info: dict) -> dict:
    """Run a single claim through the full pipeline, capture everything."""
    claim_text = claim_info['claim']
    request = ClaimRequest(claim=claim_text)

    print(f"\n{'='*60}")
    print(f"CLAIM: {claim_text}")
    print(f"Expected: {claim_info['expected_verdict']} ({claim_info['category']})")
    print(f"{'='*60}")

    # Step 1: Classify claim
    claim_type, claim_type_conf = classify_claim_type(claim_text)
    claim_domain = classify_claim_domain(claim_text)
    routing_config = build_routing_config(claim_domain, claim_text)
    print(f"  Type: {claim_type} ({claim_type_conf:.2f}), Domain: {claim_domain}")

    # Step 2: Search sources
    raw_sources = await search_sources(request, routing_config)
    raw_sources = _filter_relevant_sources(claim_text, raw_sources)
    raw_sources = _deduplicate_sources(raw_sources)
    print(f"  Sources after dedup: {len(raw_sources)}")

    # Step 3: Analyze each source with full sentence capture
    source_results = []
    for source in raw_sources:
        if not source.snippet:
            continue

        # Infer expected_stance from claim category
        if claim_info['category'] == 'factual_true':
            exp_stance = 'supporting'
        elif claim_info['category'] == 'factual_false':
            exp_stance = 'opposing'
        else:
            exp_stance = 'mixed'

        source_data = {
            'title': source.title,
            'source_type': source.source_type,
            'url': source.url,
            'word_count': len((source.snippet or '').split()),
            'snippet_preview': (source.snippet or '')[:200],
            'expected_stance': exp_stance,
            'sentences': [],
            'paragraph_nli': {},
            'stance': '',
            'stance_confidence': 0.0,
            'stance_method': '',
        }

        # Wikidata: skip NLI
        if source.source_type == "knowledge_graph":
            source_data['stance'] = 'neutral'
            source_data['stance_confidence'] = 0.0
            source_data['stance_method'] = 'wikidata_bypass'
            source_results.append(source_data)
            continue

        # Fact-check: try rating bypass
        if source.source_type == "fact_check" and source.raw_claim_rating:
            fc_stance, fc_conf = _stance_from_factcheck(source, claim_text)
            if fc_stance:
                source_data['stance'] = fc_stance
                source_data['stance_confidence'] = fc_conf
                source_data['stance_method'] = 'factcheck_rating'
                source_data['raw_rating'] = source.raw_claim_rating
                source_results.append(source_data)
                continue
            else:
                print(f"  [FC-SKIP] Rating bypass failed: {source.title[:60]}")
                continue

        # Regular source: sentence-level NLI
        premise = source.snippet if source.snippet else source.title
        stance, confidence, sent_details = classify_stance_sentences(premise, claim_text)

        source_data['stance'] = stance
        source_data['stance_confidence'] = confidence
        source_data['stance_method'] = 'sentence_nli'

        # Capture every sentence
        for sd in sent_details:
            source_data['sentences'].append({
                'text': sd['text'],
                'word_count': sd.get('word_count', len(sd['text'].split())),
                'p_supp': round(sd['p_supp'], 6),
                'p_neut': round(sd['p_neut'], 6),
                'p_opp': round(sd['p_opp'], 6),
                'label': sd['label'],
                'confidence': round(sd['confidence'], 6),
            })

        source_results.append(source_data)

    # Step 4: Build result
    result = {
        'claim': claim_text,
        'expected_verdict': claim_info['expected_verdict'],
        'category': claim_info['category'],
        'claim_type_detected': claim_type,
        'claim_type_confidence': round(claim_type_conf, 4),
        'claim_domain': claim_domain,
        'num_sources': len(source_results),
        'sources': source_results,
        'collected_at': time.strftime('%Y-%m-%d %H:%M:%S'),
    }

    total_sents = sum(len(s['sentences']) for s in source_results)
    print(f"  Collected: {len(source_results)} sources, {total_sents} sentences")
    return result


async def main():
    print("Fresh Pipeline Collection")
    print(f"Claims to process: {len(CLAIMS)}")
    print(f"Output: {RESULTS_FILE}")
    print()

    # Load any previous progress
    progress = load_progress()
    completed_claims = set(progress.keys())
    print(f"Previously completed: {len(completed_claims)} claims")

    results = dict(progress)  # Start from previous progress
    errors = []

    for i, claim_info in enumerate(CLAIMS):
        claim_text = claim_info['claim']

        if claim_text in completed_claims:
            print(f"[{i+1}/{len(CLAIMS)}] SKIP (already done): {claim_text}")
            continue

        try:
            result = await collect_claim(claim_info)
            results[claim_text] = result
            save_progress(results)
            print(f"  [{i+1}/{len(CLAIMS)}] SAVED")
        except Exception as e:
            print(f"  [{i+1}/{len(CLAIMS)}] ERROR: {e}")
            errors.append({'claim': claim_text, 'error': str(e)})

        # Brief pause between claims to avoid rate limits
        if i < len(CLAIMS) - 1:
            time.sleep(1)

    # Convert to list format and save final results
    final = []
    for claim_info in CLAIMS:
        claim_text = claim_info['claim']
        if claim_text in results:
            final.append(results[claim_text])

    with open(RESULTS_FILE, 'w') as f:
        json.dump(final, f, indent=2)

    # Also save in unified_dataset.json format for the analysis script
    unified = []
    for r in final:
        unified.append({
            'claim': r['claim'],
            'expected_verdict': r['expected_verdict'],
            'category': r['category'],
            'origin': 'fresh',
            'sources': [{
                'title': s.get('title', ''),
                'source_type': s.get('source_type', ''),
                'url': s.get('url', ''),
                'word_count': s.get('word_count', 0),
                'paragraph_nli': s.get('paragraph_nli', {}),
                'sentences': s.get('sentences', []),
                'expected_stance': s.get('expected_stance', 'mixed'),
                'origin': 'fresh',
            } for s in r['sources']],
        })
    unified_path = OUTPUT_DIR / "unified_dataset.json"
    with open(unified_path, 'w') as f:
        json.dump(unified, f, indent=2)
    print(f"Unified dataset saved to: {unified_path}")

    print(f"\n{'='*60}")
    print(f"COLLECTION COMPLETE")
    print(f"{'='*60}")
    print(f"Successful: {len(final)}/{len(CLAIMS)}")
    print(f"Errors: {len(errors)}")
    if errors:
        print("Failed claims:")
        for e in errors:
            print(f"  {e['claim']}: {e['error']}")
    print(f"Results saved to: {RESULTS_FILE}")

    # Clean up progress file
    if len(errors) == 0 and PROGRESS_FILE.exists():
        os.remove(PROGRESS_FILE)
        print("Progress file cleaned up.")


if __name__ == "__main__":
    asyncio.run(main())