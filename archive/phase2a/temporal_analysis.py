"""
Temporal Analysis Data Extraction

Runs the full pipeline and outputs a CSV with every surviving source,
its full snippet, NLI result, and extracted temporal signals.

Usage:
  python temporal_analysis.py              # all 36 claims
  python temporal_analysis.py --quick 5    # 5 random claims

Output: tests/temporal_analysis.csv
"""

import argparse
import asyncio
import csv
import os
import random
import re
from datetime import datetime

from app.models.schemas import ClaimRequest, Source
from app.services.google_factcheck import search_factcheck
from app.services.wikipedia import search_wikipedia
from app.services.semantic_scholar import search_semantic_scholar
from app.services.open_alex import search_openalex
from app.services.duckduckgo import search_duckduckgo
from app.services.wikidata import search_wikidata
from app.services.nli_service import classify_stance, compute_relevance
from app.services.claim_classifier import classify_claim_type, classify_claim_domain
from app.services.source_router import build_routing_config
from app.services.claim_service import (
    _stance_from_factcheck,
    _deduplicate_sources,
    RELEVANCE_THRESHOLD,
)


TEST_CLAIMS = [
    {"claim": "climate change is real", "expected_verdict": "strongly supported", "category": "factual_true"},
    {"claim": "evolution is real", "expected_verdict": "strongly supported", "category": "factual_true"},
    {"claim": "water boils at 100 degrees celsius", "expected_verdict": "strongly supported", "category": "factual_true"},
    {"claim": "the speed of light is constant", "expected_verdict": "strongly supported", "category": "factual_true"},
    {"claim": "the earth is flat", "expected_verdict": "strongly opposed", "category": "factual_false"},
    {"claim": "vaccines cause autism", "expected_verdict": "strongly opposed", "category": "factual_false"},
    {"claim": "the moon landing was faked", "expected_verdict": "strongly opposed", "category": "factual_false"},
    {"claim": "5G causes COVID", "expected_verdict": "strongly opposed", "category": "factual_false"},
    {"claim": "LeBron James is the greatest basketball player of all time", "expected_verdict": "opinion", "category": "opinion"},
    {"claim": "pineapple belongs on pizza", "expected_verdict": "opinion", "category": "opinion"},
    {"claim": "democracy is the best form of government", "expected_verdict": "opinion", "category": "opinion"},
    {"claim": "sugar is worse than fat for health", "expected_verdict": "contested", "category": "contested"},
    {"claim": "nuclear energy is safe", "expected_verdict": "contested", "category": "contested"},
    {"claim": "remote work is more productive than office work", "expected_verdict": "contested", "category": "contested"},
    {"claim": "AI will replace most jobs", "expected_verdict": "contested", "category": "current_event"},
    {"claim": "the United States economy is in a recession", "expected_verdict": "contested", "category": "current_event"},
    {"claim": "violent video games cause real world violence", "expected_verdict": "contested", "category": "contested"},
    {"claim": "smoking causes lung cancer", "expected_verdict": "strongly supported", "category": "factual_true"},
    {"claim": "capitalism is better than socialism", "expected_verdict": "opinion", "category": "opinion"},
    {"claim": "we only use 10% of our brains", "expected_verdict": "strongly opposed", "category": "factual_false"},
    {"claim": "social media is harmful to mental health", "expected_verdict": "contested", "category": "contested"},
    {"claim": "the Beatles are the greatest band of all time", "expected_verdict": "opinion", "category": "opinion"},
    {"claim": "antibiotics do not work against viruses", "expected_verdict": "strongly supported", "category": "factual_true"},
    {"claim": "goldfish have a 3 second memory", "expected_verdict": "strongly opposed", "category": "factual_false"},
    {"claim": "immigration is good for the economy", "expected_verdict": "contested", "category": "contested"},
    {"claim": "the Great Wall of China is visible from space", "expected_verdict": "strongly opposed", "category": "factual_false"},
    {"claim": "cats are better pets than dogs", "expected_verdict": "opinion", "category": "opinion"},
    {"claim": "organic food is healthier than conventional food", "expected_verdict": "contested", "category": "contested"},
    {"claim": "MSG is dangerous to consume", "expected_verdict": "strongly opposed", "category": "factual_false"},
    {"claim": "humans share about 98% of DNA with chimpanzees", "expected_verdict": "strongly supported", "category": "factual_true"},
    {"claim": "China has the world's largest economy", "expected_verdict": "contested", "category": "current_event"},
    {"claim": "eating carrots improves your eyesight", "expected_verdict": "strongly opposed", "category": "factual_false"},
    {"claim": "college education is worth the cost", "expected_verdict": "opinion", "category": "opinion"},
    {"claim": "inflation in the United States is under control", "expected_verdict": "contested", "category": "current_event"},
    {"claim": "the Amazon rainforest produces about 20% of the world's oxygen", "expected_verdict": "strongly opposed", "category": "factual_false"},
    {"claim": "the Great Wall of China is the only man-made structure visible from space", "expected_verdict": "strongly opposed", "category": "factual_false"},
]


# -- Temporal signal extraction ------------------------------------------------

YEAR_PATTERN = re.compile(r'\b((?:19|20)\d{2})\b')

PAST_EVENT_PATTERNS = [
    re.compile(r'\b(?:in|during|since|after|before|by)\s+((?:19|20)\d{2})\b', re.IGNORECASE),
    re.compile(r'\b((?:19|20)\d{2})\s+(?:recession|crisis|pandemic|election|war|crash)\b', re.IGNORECASE),
    re.compile(r'\b(?:formerly|previously|at that time|back then)\b', re.IGNORECASE),
]

RECENCY_PATTERNS = [
    re.compile(r'\b(?:currently|now|today|this year|this month|recently|latest|newest)\b', re.IGNORECASE),
]

TENSE_PAST_PATTERNS = [
    re.compile(r'\b(?:was|were|had been|used to be|formerly|previously)\b', re.IGNORECASE),
]


def extract_temporal_signals(text: str) -> dict:
    """Extract all temporal signals from source text."""
    years = YEAR_PATTERN.findall(text)
    years_int = sorted(set(int(y) for y in years if 1900 <= int(y) <= 2030))

    past_events = []
    for pat in PAST_EVENT_PATTERNS:
        past_events.extend(pat.findall(text))

    recency_words = []
    for pat in RECENCY_PATTERNS:
        recency_words.extend(pat.findall(text))

    past_tense = []
    for pat in TENSE_PAST_PATTERNS:
        past_tense.extend(pat.findall(text))

    # Compute temporal spread
    min_year = min(years_int) if years_int else None
    max_year = max(years_int) if years_int else None
    year_spread = (max_year - min_year) if (min_year and max_year) else 0

    return {
        "years_mentioned": ";".join(str(y) for y in years_int),
        "year_count": len(years_int),
        "min_year": min_year or "",
        "max_year": max_year or "",
        "year_spread": year_spread,
        "past_event_signals": ";".join(str(p) for p in past_events[:5]),
        "recency_signals": ";".join(recency_words[:5]),
        "past_tense_count": len(past_tense),
        "recency_count": len(recency_words),
    }


# -- Pipeline (reused from test_baseline) -------------------------------------

API_FUNCTIONS = {
    "google_factcheck": lambda req, cfg: search_factcheck(req),
    "wikipedia":        lambda req, cfg: search_wikipedia(req),
    "semantic_scholar":  lambda req, cfg: search_semantic_scholar(req, cfg),
    "open_alex":        lambda req, cfg: search_openalex(req, cfg),
    "duckduckgo":       lambda req, cfg: search_duckduckgo(req),
    "wikidata":         lambda req, cfg: search_wikidata(req),
}


async def fetch_sources_by_api(request, routing_config):
    api_sources = {}
    tasks = {}
    for api_name, func in API_FUNCTIONS.items():
        cfg = routing_config.get(api_name, {})
        if cfg.get("skip"):
            api_sources[api_name] = {"skipped": True}
            continue
        tasks[api_name] = func(request, cfg)

    if tasks:
        results = await asyncio.gather(*[t for t in tasks.values()], return_exceptions=True)
        for api_name, result in zip(tasks.keys(), results):
            if isinstance(result, Exception):
                api_sources[api_name] = {"error": str(result)}
            else:
                api_sources[api_name] = result
    return api_sources


def get_nli_result(source: Source, claim: str) -> dict:
    """Get NLI result for a source."""
    if source.source_type == "knowledge_graph":
        return {"method": "wikidata_skip", "stance": "", "confidence": 0}

    if source.source_type == "fact_check" and source.raw_claim_rating:
        fc_stance, fc_conf = _stance_from_factcheck(source, claim)
        meta = source.metadata or {}
        if fc_stance:
            return {
                "method": "factcheck_rating_bypass",
                "stance": fc_stance,
                "confidence": fc_conf,
                "raw_claim_rating": source.raw_claim_rating,
                "review_date": meta.get("review_date", ""),
                "claim_date": meta.get("claim_date", ""),
                "publisher_name": meta.get("publisher_name", ""),
            }
        return {
            "method": "fc_skip",
            "stance": "",
            "confidence": 0,
            "raw_claim_rating": source.raw_claim_rating,
            "review_date": meta.get("review_date", ""),
            "claim_date": meta.get("claim_date", ""),
            "publisher_name": meta.get("publisher_name", ""),
        }

    premise = source.snippet if source.snippet else source.title
    if not premise:
        return {"method": "skipped", "stance": "", "confidence": 0}

    stance, confidence = classify_stance(premise, claim)
    return {"method": "nli_deberta", "stance": stance, "confidence": round(confidence, 4)}


async def process_claim(claim_data: dict) -> list[dict]:
    """Run one claim through pipeline, return list of source rows for CSV."""
    claim_text = claim_data["claim"]
    request = ClaimRequest(claim=claim_text)

    claim_type, ct_conf = classify_claim_type(claim_text)
    claim_domain = classify_claim_domain(claim_text)
    routing_config = build_routing_config(claim_domain, claim_text)

    # Fetch sources
    api_sources = await fetch_sources_by_api(request, routing_config)
    all_sources = []
    source_origins = {}
    for api_name, sources in api_sources.items():
        if isinstance(sources, (dict, type(None))):
            continue
        for s in sources:
            all_sources.append(s)
            source_origins[id(s)] = api_name

    # Relevance filter
    if all_sources:
        from app.services.nli_service import compute_relevance as cr
        texts = [(s.title or "") + " " + (s.snippet or "") for s in all_sources]
        scores = cr(claim_text, texts)
        kept = [(s, sc) for s, sc in zip(all_sources, scores) if sc >= RELEVANCE_THRESHOLD]
        filtered = [s for s, _ in kept]
        relevance_scores = {id(s): sc for s, sc in kept}
    else:
        filtered = []
        relevance_scores = {}

    # Dedup
    deduped = _deduplicate_sources(filtered)

    # Build rows
    rows = []
    for source in deduped:
        nli = get_nli_result(source, claim_text)
        temporal = extract_temporal_signals(source.snippet or "")
        meta = source.metadata or {}

        row = {
            # Claim info
            "claim": claim_text,
            "category": claim_data["category"],
            "expected_verdict": claim_data["expected_verdict"],
            "claim_type": claim_type,
            "claim_domain": claim_domain,
            # Source info
            "source_type": source.source_type,
            "origin_api": source_origins.get(id(source), "unknown"),
            "title": source.title or "",
            "url": source.url or "",
            "relevance_score": round(relevance_scores.get(id(source), 0), 4),
            # Full snippet (NOT truncated)
            "snippet_full": source.snippet or "",
            "snippet_word_count": len((source.snippet or "").split()),
            # NLI
            "nli_method": nli["method"],
            "nli_stance": nli.get("stance", ""),
            "nli_confidence": nli.get("confidence", 0),
            # FC-specific
            "fc_rating": nli.get("raw_claim_rating", ""),
            "fc_review_date": nli.get("review_date", meta.get("review_date", "")),
            "fc_claim_date": nli.get("claim_date", meta.get("claim_date", "")),
            "fc_publisher": nli.get("publisher_name", meta.get("publisher_name", "")),
            "enriched": meta.get("enriched", ""),
            # Temporal signals
            **temporal,
        }
        rows.append(row)

    return rows


async def main():
    parser = argparse.ArgumentParser(description="Temporal analysis data extraction")
    parser.add_argument("--quick", type=int, metavar="N",
                        help="Run N random claims instead of all")
    args = parser.parse_args()

    claims = TEST_CLAIMS[:]
    if args.quick:
        claims = random.sample(claims, min(args.quick, len(claims)))
        print(f"Quick mode: {len(claims)} claims")

    os.makedirs("tests", exist_ok=True)
    print(f"Extracting temporal analysis data for {len(claims)} claims...")
    print(f"This will take a few minutes (API calls + NLI per claim).\n")

    all_rows = []
    for i, claim_data in enumerate(claims, 1):
        print(f"[{i}/{len(claims)}] {claim_data['claim']}")
        try:
            rows = await process_claim(claim_data)
            all_rows.extend(rows)
            print(f"  -> {len(rows)} sources captured")
        except Exception as e:
            print(f"  -> ERROR: {e}")

    # Write CSV
    csv_path = "tests/temporal_analysis.csv"
    if all_rows:
        fieldnames = list(all_rows[0].keys())
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(all_rows)

    print(f"\nDone. {len(all_rows)} source rows written to {csv_path}")
    print(f"Open in Excel/Google Sheets to analyze temporal patterns.")

    # Quick summary
    with_years = sum(1 for r in all_rows if r["year_count"] > 0)
    print(f"\nSources with year mentions: {with_years}/{len(all_rows)}")
    by_type = {}
    for r in all_rows:
        st = r["source_type"]
        if st not in by_type:
            by_type[st] = 0
        by_type[st] += 1
    print("By source type:", by_type)


if __name__ == "__main__":
    asyncio.run(main())