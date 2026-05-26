"""
Phase 1 Implementation Validation

Tests each Phase 1 step by comparing WITH vs WITHOUT the improvement.
This is NOT an NLI model test. This tests the PIPELINE steps we built.

Tests:
  1. Claim classifier accuracy (Step 1)
  2. Source routing correctness (Step 1)
  3. Dedup effectiveness (Step 2)
  4. FC bypass vs raw NLI comparison (Step 5)
  5. Enrichment impact: enriched snippet vs original snippet NLI (Steps 3-5)
  6. Content extractor scoring (Steps 3-5)

Usage:
  python phase1_validation.py

Output: tests/phase1_validation_report.md
"""

import asyncio
import csv
import os
import re
from datetime import datetime
from collections import Counter, defaultdict

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
    _is_non_content,
    _deduplicate_sources,
    RELEVANCE_THRESHOLD,
)

# -- Test Claims with expected classifications ---------------------------------

CLASSIFIER_TESTS = [
    # (claim, expected_category, acceptable_types, expected_domain)
    ("climate change is real", "factual_true", ["factual"], "scientific"),
    ("evolution is real", "factual_true", ["factual"], "scientific"),
    ("the earth is flat", "factual_false", ["factual"], "scientific"),
    ("vaccines cause autism", "factual_false", ["factual"], "scientific"),
    ("the moon landing was faked", "factual_false", ["factual"], "historical"),
    ("5G causes COVID", "factual_false", ["factual"], "scientific"),
    ("LeBron James is the greatest basketball player of all time", "opinion", ["opinion"], "general"),
    ("pineapple belongs on pizza", "opinion", ["opinion"], "general"),
    ("democracy is the best form of government", "opinion", ["opinion"], "general"),
    ("sugar is worse than fat for health", "contested", ["factual", "opinion"], "scientific"),
    ("nuclear energy is safe", "contested", ["factual", "opinion"], "scientific"),
    ("AI will replace most jobs", "current_event", ["factual", "opinion"], "current_events"),
    ("the United States economy is in a recession", "current_event", ["factual"], "current_events"),
    ("smoking causes lung cancer", "factual_true", ["factual"], "scientific"),
    ("capitalism is better than socialism", "opinion", ["opinion"], "general"),
    ("goldfish have a 3 second memory", "factual_false", ["factual"], "general"),
    ("eating carrots improves your eyesight", "factual_false", ["factual"], "general"),
    ("China has the world's largest economy", "current_event", ["factual"], "current_events"),
    ("inflation in the United States is under control", "current_event", ["factual"], "current_events"),
]


# -- Test 1: Claim Classifier -------------------------------------------------

def test_classifier():
    """Test claim type and domain classification accuracy."""
    print("\n" + "=" * 70)
    print("TEST 1: CLAIM CLASSIFIER ACCURACY")
    print("=" * 70)

    type_correct = 0
    domain_correct = 0
    type_errors = []
    domain_errors = []

    for claim, category, acceptable_types, expected_domain in CLASSIFIER_TESTS:
        ct, ct_conf = classify_claim_type(claim)
        cd = classify_claim_domain(claim)

        type_ok = ct in acceptable_types
        domain_ok = cd == expected_domain

        if type_ok:
            type_correct += 1
        else:
            type_errors.append(f"  '{claim[:50]}': got {ct}, expected one of {acceptable_types}")

        if domain_ok:
            domain_correct += 1
        else:
            domain_errors.append(f"  '{claim[:50]}': got {cd}, expected {expected_domain}")

    total = len(CLASSIFIER_TESTS)
    print(f"\n  Claim TYPE accuracy:   {type_correct}/{total} ({100*type_correct/total:.1f}%)")
    if type_errors:
        print("  Type errors:")
        for e in type_errors:
            print(e)

    print(f"\n  Claim DOMAIN accuracy: {domain_correct}/{total} ({100*domain_correct/total:.1f}%)")
    if domain_errors:
        print("  Domain errors:")
        for e in domain_errors:
            print(e)

    return {
        "type_accuracy": f"{type_correct}/{total}",
        "domain_accuracy": f"{domain_correct}/{total}",
        "type_errors": type_errors,
        "domain_errors": domain_errors,
    }


# -- Test 2: Source Routing ----------------------------------------------------

def test_routing():
    """Verify source routing skips irrelevant APIs correctly."""
    print("\n" + "=" * 70)
    print("TEST 2: SOURCE ROUTING CORRECTNESS")
    print("=" * 70)

    routing_tests = [
        # (claim, domain, should_skip, should_include)
        ("pineapple belongs on pizza", "general", ["semantic_scholar", "open_alex"], ["duckduckgo", "wikipedia"]),
        ("climate change is real", "scientific", [], ["semantic_scholar", "open_alex", "duckduckgo", "wikipedia"]),
        ("the moon landing was faked", "historical", ["semantic_scholar"], ["duckduckgo", "wikipedia", "google_factcheck"]),
    ]

    correct = 0
    errors = []

    for claim, domain, should_skip, should_include in routing_tests:
        config = build_routing_config(domain, claim)

        for api in should_skip:
            api_conf = config.get(api, {})
            if api_conf.get("skip"):
                correct += 1
            else:
                errors.append(f"  '{claim[:40]}': {api} should be SKIPPED but isn't")

        for api in should_include:
            api_conf = config.get(api, {})
            if not api_conf.get("skip"):
                correct += 1
            else:
                errors.append(f"  '{claim[:40]}': {api} should be INCLUDED but is skipped")

    total = correct + len(errors)
    print(f"\n  Routing rules: {correct}/{total} correct")
    if errors:
        print("  Errors:")
        for e in errors:
            print(e)

    return {"routing_correct": f"{correct}/{total}", "errors": errors}


# -- Test 3: Dedup Effectiveness -----------------------------------------------

def test_dedup():
    """Test dedup with synthetic duplicate sources."""
    print("\n" + "=" * 70)
    print("TEST 3: DEDUP EFFECTIVENESS")
    print("=" * 70)

    # Create synthetic sources with known duplicates
    sources = [
        Source(url="https://example.com/article1", title="Climate Change Evidence",
               snippet="Evidence shows warming", source_type="web", raw_claim_rating=None, metadata={}),
        # URL duplicate (different title, same URL)
        Source(url="https://example.com/article1", title="Climate Evidence Report",
               snippet="Different snippet", source_type="web", raw_claim_rating=None, metadata={}),
        # Title near-duplicate
        Source(url="https://example2.com/article2", title="Climate Change Evidence!",
               snippet="More evidence", source_type="web", raw_claim_rating=None, metadata={}),
        # Content duplicate (same first 200 chars)
        Source(url="https://example3.com/article3", title="Unique Title",
               snippet="Evidence shows warming", source_type="web", raw_claim_rating=None, metadata={}),
        # Genuinely unique
        Source(url="https://example4.com/article4", title="Solar Panel Efficiency",
               snippet="Solar panels are getting cheaper", source_type="web", raw_claim_rating=None, metadata={}),
        # Higher priority duplicate (fact_check should beat web)
        Source(url="https://example.com/article1", title="FC: Climate Change",
               snippet="FC content", source_type="fact_check", raw_claim_rating="True", metadata={}),
    ]

    before = len(sources)
    deduped = _deduplicate_sources(sources)
    after = len(deduped)
    removed = before - after

    print(f"\n  Before dedup: {before} sources")
    print(f"  After dedup:  {after} sources")
    print(f"  Removed:      {removed}")

    # Verify the right ones survived
    deduped_urls = [s.url for s in deduped]
    deduped_types = [s.source_type for s in deduped]

    checks = []
    # URL dedup should keep higher priority (fact_check > web)
    if "https://example.com/article1" in deduped_urls:
        fc_survived = any(s.source_type == "fact_check" and s.url == "https://example.com/article1" for s in deduped)
        web_survived = any(s.source_type == "web" and s.url == "https://example.com/article1" for s in deduped)
        checks.append(("URL dedup keeps higher priority", fc_survived and not web_survived))

    # Unique source should survive
    unique_survived = any(s.url == "https://example4.com/article4" for s in deduped)
    checks.append(("Unique source survives", unique_survived))

    for name, passed in checks:
        status = "PASS" if passed else "FAIL"
        print(f"  [{status}] {name}")

    return {"before": before, "after": after, "checks": checks}


# -- Test 4: FC Bypass vs Raw NLI Comparison -----------------------------------

async def test_fc_bypass_vs_nli():
    """For FC sources, compare bypass result vs what NLI would give.
    This tests: is FC bypass actually better than running NLI?"""
    print("\n" + "=" * 70)
    print("TEST 4: FC BYPASS vs RAW NLI (A/B Comparison)")
    print("=" * 70)

    test_claims = [
        {"claim": "climate change is real", "expected": "strongly supported"},
        {"claim": "the earth is flat", "expected": "strongly opposed"},
        {"claim": "vaccines cause autism", "expected": "strongly opposed"},
        {"claim": "5G causes COVID", "expected": "strongly opposed"},
        {"claim": "the moon landing was faked", "expected": "strongly opposed"},
        {"claim": "smoking causes lung cancer", "expected": "strongly supported"},
    ]

    bypass_correct = 0
    bypass_wrong = 0
    nli_correct = 0
    nli_wrong = 0
    nli_would_skip = 0  # sources NLI can't handle well
    comparisons = []

    for tc in test_claims:
        request = ClaimRequest(claim=tc["claim"])
        fc_sources = await search_factcheck(request)

        for source in fc_sources:
            if not source.raw_claim_rating:
                continue

            expected = tc["expected"]

            # A) What bypass gives
            bypass_stance, bypass_conf = _stance_from_factcheck(source, tc["claim"])

            # B) What NLI would give on the FC snippet
            premise = source.snippet if source.snippet else source.title
            if premise:
                nli_stance, nli_conf = classify_stance(premise, tc["claim"])
            else:
                nli_stance, nli_conf = "neutral", 0.0

            # Judge correctness
            def is_correct(stance, expected):
                if not stance:
                    return False
                if expected in ("strongly supported", "likely supported"):
                    return stance == "supporting"
                elif expected in ("strongly opposed", "likely opposed"):
                    return stance == "opposing"
                return True  # can't judge contested/opinion

            bypass_ok = is_correct(bypass_stance, expected) if bypass_stance else False
            nli_ok = is_correct(nli_stance, expected)

            if bypass_stance:
                if bypass_ok:
                    bypass_correct += 1
                else:
                    bypass_wrong += 1

            if nli_ok:
                nli_correct += 1
            else:
                nli_wrong += 1

            comparisons.append({
                "claim": tc["claim"][:40],
                "rating": source.raw_claim_rating[:30] if source.raw_claim_rating else "",
                "bypass": f"{bypass_stance or 'DROPPED'}",
                "nli": f"{nli_stance}",
                "bypass_ok": bypass_ok if bypass_stance else "dropped",
                "nli_ok": nli_ok,
                "publisher": (source.metadata or {}).get("publisher_name", ""),
            })

    bypass_total = bypass_correct + bypass_wrong
    nli_total = nli_correct + nli_wrong

    print(f"\n  FC sources compared: {len(comparisons)}")
    print(f"\n  BYPASS accuracy: {bypass_correct}/{bypass_total} ({100*bypass_correct/max(bypass_total,1):.1f}%) + {len(comparisons)-bypass_total} dropped")
    print(f"  RAW NLI accuracy: {nli_correct}/{nli_total} ({100*nli_correct/max(nli_total,1):.1f}%)")

    improvement = (bypass_correct/max(bypass_total,1)) - (nli_correct/max(nli_total,1))
    print(f"\n  Bypass improvement over NLI: {improvement*100:+.1f} percentage points")

    if improvement > 0:
        print(f"  VERDICT: FC bypass is BETTER than raw NLI -> Step 5 JUSTIFIED")
    elif improvement == 0:
        print(f"  VERDICT: FC bypass same as NLI -> Step 5 NEUTRAL")
    else:
        print(f"  VERDICT: FC bypass WORSE than NLI -> Step 5 NEEDS REVIEW")

    # Show disagreements
    disagreements = [c for c in comparisons if c["bypass_ok"] != c["nli_ok"] and c["bypass_ok"] != "dropped"]
    if disagreements:
        print(f"\n  Cases where bypass and NLI disagree ({len(disagreements)}):")
        for d in disagreements[:10]:
            print(f"    '{d['claim']}' [{d['publisher'][:15]}] bypass={d['bypass']}({d['bypass_ok']}) nli={d['nli']}({d['nli_ok']}) rating='{d['rating']}'")

    return {
        "bypass_accuracy": f"{bypass_correct}/{bypass_total}",
        "nli_accuracy": f"{nli_correct}/{nli_total}",
        "improvement": f"{improvement*100:+.1f}pp",
    }


# -- Test 5: Enrichment Impact ------------------------------------------------

async def test_enrichment_impact():
    """Compare NLI on original vs enriched snippets.
    Tests: does content_extractor enrichment improve NLI accuracy?"""
    print("\n" + "=" * 70)
    print("TEST 5: ENRICHMENT IMPACT (Original vs Enriched Snippet)")
    print("=" * 70)

    test_claims = [
        {"claim": "climate change is real", "expected": "strongly supported"},
        {"claim": "vaccines cause autism", "expected": "strongly opposed"},
        {"claim": "the earth is flat", "expected": "strongly opposed"},
        {"claim": "smoking causes lung cancer", "expected": "strongly supported"},
        {"claim": "eating carrots improves your eyesight", "expected": "strongly opposed"},
        {"claim": "goldfish have a 3 second memory", "expected": "strongly opposed"},
    ]

    original_correct = 0
    enriched_correct = 0
    original_total = 0
    enriched_total = 0
    improvements = []

    for tc in test_claims:
        request = ClaimRequest(claim=tc["claim"])

        # Get DDG sources (have both original and enriched)
        ddg_sources = await search_duckduckgo(request)
        wiki_sources = await search_wikipedia(request)

        for source in ddg_sources + wiki_sources:
            meta = source.metadata or {}
            enriched = meta.get("enriched", False)
            original_snippet = meta.get("ddg_snippet", meta.get("intro_extract", ""))
            enriched_snippet = source.snippet

            if not enriched or not original_snippet or not enriched_snippet:
                continue
            if len(original_snippet.split()) < 10:
                continue

            expected = tc["expected"]

            # NLI on original
            orig_stance, orig_conf = classify_stance(original_snippet, tc["claim"])
            # NLI on enriched
            enr_stance, enr_conf = classify_stance(enriched_snippet, tc["claim"])

            def is_correct(stance, expected):
                if expected in ("strongly supported", "likely supported"):
                    return stance == "supporting"
                elif expected in ("strongly opposed", "likely opposed"):
                    return stance == "opposing"
                return True

            orig_ok = is_correct(orig_stance, expected)
            enr_ok = is_correct(enr_stance, expected)

            original_total += 1
            enriched_total += 1
            if orig_ok:
                original_correct += 1
            if enr_ok:
                enriched_correct += 1

            if orig_ok != enr_ok:
                direction = "IMPROVED" if enr_ok else "REGRESSED"
                improvements.append({
                    "claim": tc["claim"][:40],
                    "title": source.title[:50],
                    "direction": direction,
                    "original": orig_stance,
                    "enriched": enr_stance,
                    "source_type": source.source_type,
                })

    print(f"\n  Sources compared: {original_total}")
    print(f"  Original snippet NLI accuracy: {original_correct}/{original_total} ({100*original_correct/max(original_total,1):.1f}%)")
    print(f"  Enriched snippet NLI accuracy: {enriched_correct}/{enriched_total} ({100*enriched_correct/max(enriched_total,1):.1f}%)")

    improvement = (enriched_correct/max(enriched_total,1)) - (original_correct/max(original_total,1))
    print(f"\n  Enrichment improvement: {improvement*100:+.1f} percentage points")

    improved = [i for i in improvements if i["direction"] == "IMPROVED"]
    regressed = [i for i in improvements if i["direction"] == "REGRESSED"]
    print(f"  Individual changes: {len(improved)} improved, {len(regressed)} regressed")

    if improved:
        print(f"\n  Improved cases:")
        for i in improved[:8]:
            print(f"    [{i['source_type'][:8]}] '{i['claim']}' | {i['original']} -> {i['enriched']}")
    if regressed:
        print(f"\n  Regressed cases:")
        for i in regressed[:8]:
            print(f"    [{i['source_type'][:8]}] '{i['claim']}' | {i['original']} -> {i['enriched']}")

    return {
        "original_accuracy": f"{original_correct}/{original_total}",
        "enriched_accuracy": f"{enriched_correct}/{enriched_total}",
        "improvement": f"{improvement*100:+.1f}pp",
        "improved_count": len(improved),
        "regressed_count": len(regressed),
    }


# -- Test 6: Extract Score Quality ---------------------------------------------

async def test_extract_scores():
    """Verify content_extractor produces meaningful scores."""
    print("\n" + "=" * 70)
    print("TEST 6: CONTENT EXTRACTOR SCORING")
    print("=" * 70)

    test_claims = [
        "climate change is real",
        "vaccines cause autism",
        "the earth is flat",
    ]

    fc_scores = []
    ddg_scores = []
    wiki_scores = []

    for claim_text in test_claims:
        request = ClaimRequest(claim=claim_text)
        fc = await search_factcheck(request)
        ddg = await search_duckduckgo(request)
        wiki = await search_wikipedia(request)

        for s in fc:
            es = (s.metadata or {}).get("extract_score")
            if es is not None:
                fc_scores.append(es)
        for s in ddg:
            es = (s.metadata or {}).get("extract_score")
            if es is not None:
                ddg_scores.append(es)
        for s in wiki:
            es = (s.metadata or {}).get("extract_score")
            if es is not None:
                wiki_scores.append(es)

    for name, scores in [("FC", fc_scores), ("DDG", ddg_scores), ("Wiki", wiki_scores)]:
        if not scores:
            print(f"\n  {name}: no scores available")
            continue
        nonzero = [s for s in scores if s > 0]
        print(f"\n  {name} ({len(scores)} sources):")
        print(f"    Nonzero: {len(nonzero)}/{len(scores)} ({100*len(nonzero)/len(scores):.0f}%)")
        if nonzero:
            print(f"    Range: {min(nonzero):.3f} to {max(nonzero):.3f}")
            print(f"    Mean: {sum(nonzero)/len(nonzero):.3f}")
        zero_count = len(scores) - len(nonzero)
        if zero_count > 0:
            print(f"    Zero scores: {zero_count} (likely single-paragraph articles)")

    return {"fc_scores": len(fc_scores), "ddg_scores": len(ddg_scores), "wiki_scores": len(wiki_scores)}


# -- Main ----------------------------------------------------------------------

async def main():
    os.makedirs("tests", exist_ok=True)
    lines = []
    lines.append("# Phase 1 Implementation Validation")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")

    # Test 1: Classifier
    r1 = test_classifier()
    lines.append(f"## Test 1: Claim Classifier")
    lines.append(f"Type accuracy: {r1['type_accuracy']}")
    lines.append(f"Domain accuracy: {r1['domain_accuracy']}")
    if r1['type_errors']:
        lines.append("Type errors: " + "; ".join(r1['type_errors']))
    if r1['domain_errors']:
        lines.append("Domain errors: " + "; ".join(r1['domain_errors']))
    lines.append("")

    # Test 2: Routing
    r2 = test_routing()
    lines.append(f"## Test 2: Source Routing")
    lines.append(f"Routing correct: {r2['routing_correct']}")
    lines.append("")

    # Test 3: Dedup
    r3 = test_dedup()
    lines.append(f"## Test 3: Dedup")
    lines.append(f"Before: {r3['before']}, After: {r3['after']}")
    for name, passed in r3['checks']:
        lines.append(f"  {'PASS' if passed else 'FAIL'}: {name}")
    lines.append("")

    # Test 4: FC Bypass vs NLI
    print("\nRunning FC bypass vs NLI comparison (requires API calls + NLI)...")
    r4 = await test_fc_bypass_vs_nli()
    lines.append(f"## Test 4: FC Bypass vs Raw NLI")
    lines.append(f"Bypass accuracy: {r4['bypass_accuracy']}")
    lines.append(f"Raw NLI accuracy: {r4['nli_accuracy']}")
    lines.append(f"Improvement: {r4['improvement']}")
    lines.append("")

    # Test 5: Enrichment Impact
    print("\nRunning enrichment impact test (requires API calls + NLI)...")
    r5 = await test_enrichment_impact()
    lines.append(f"## Test 5: Enrichment Impact")
    lines.append(f"Original snippet accuracy: {r5['original_accuracy']}")
    lines.append(f"Enriched snippet accuracy: {r5['enriched_accuracy']}")
    lines.append(f"Improvement: {r5['improvement']}")
    lines.append(f"Individual: {r5['improved_count']} improved, {r5['regressed_count']} regressed")
    lines.append("")

    # Test 6: Extract Scores
    print("\nRunning extract score test...")
    r6 = await test_extract_scores()
    lines.append(f"## Test 6: Extract Scores")
    lines.append(f"FC: {r6['fc_scores']} scored, DDG: {r6['ddg_scores']} scored, Wiki: {r6['wiki_scores']} scored")
    lines.append("")

    # Save report
    report_path = "tests/phase1_validation_report.md"
    with open(report_path, "w") as f:
        f.write("\n".join(lines))
    print(f"\nReport saved to {report_path}")

    # Print summary
    print(f"\n{'='*70}")
    print("PHASE 1 VALIDATION SUMMARY")
    print(f"{'='*70}")
    print(f"  1. Classifier:  {r1['type_accuracy']} type, {r1['domain_accuracy']} domain")
    print(f"  2. Routing:     {r2['routing_correct']}")
    print(f"  3. Dedup:       {r3['before']} -> {r3['after']}")
    print(f"  4. FC Bypass:   {r4['improvement']} vs raw NLI")
    print(f"  5. Enrichment:  {r5['improvement']} from content_extractor")
    print(f"  6. Scoring:     FC={r6['fc_scores']}, DDG={r6['ddg_scores']}, Wiki={r6['wiki_scores']}")


if __name__ == "__main__":
    asyncio.run(main())