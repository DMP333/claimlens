"""
Test Baseline Runner
Runs claims through the full pipeline, captures every intermediate decision,
and outputs a detailed JSON + markdown report for diagnosing issues.

Usage: python test_baseline.py
Output: tests/baseline_results.json, tests/baseline_report.md

Place this file in your project root (same level as app/).
"""

import asyncio
import json
import os
from datetime import date, datetime

from app.models.schemas import ClaimRequest, Source
from app.services.google_factcheck import search_factcheck
from app.services.wikipedia import search_wikipedia
from app.services.semantic_scholar import search_semantic_scholar
from app.services.open_alex import search_openalex
from app.services.duckduckgo import search_duckduckgo
from app.services.wikidata import search_wikidata
from app.services.nli_service import classify_stance, classify_claim_type, compute_relevance
from app.services.credibility_service import score_all_sources
from app.services.claim_service import (
    _stance_from_factcheck,
    _is_non_content,
    _deduplicate_sources,
    RELEVANCE_THRESHOLD,
)


# ── Test Claims ──────────────────────────────────────────────────────────────

TEST_CLAIMS = [
    # Factual true (system should return "strongly supported" or "likely supported")
    {"claim": "climate change is real", "expected_verdict": "strongly supported", "category": "factual_true"},
    {"claim": "evolution is real", "expected_verdict": "strongly supported", "category": "factual_true"},
    {"claim": "water boils at 100 degrees celsius", "expected_verdict": "strongly supported", "category": "factual_true"},
    {"claim": "the speed of light is constant", "expected_verdict": "strongly supported", "category": "factual_true"},

    # Factual false / debunked (system should return "strongly opposed" or "likely opposed")
    {"claim": "the earth is flat", "expected_verdict": "strongly opposed", "category": "factual_false"},
    {"claim": "vaccines cause autism", "expected_verdict": "strongly opposed", "category": "factual_false"},
    {"claim": "the moon landing was faked", "expected_verdict": "strongly opposed", "category": "factual_false"},
    {"claim": "5G causes COVID", "expected_verdict": "strongly opposed", "category": "factual_false"},

    # Opinions (system should return opinion verdicts, never hard true/false)
    {"claim": "LeBron James is the greatest basketball player of all time", "expected_verdict": "opinion", "category": "opinion"},
    {"claim": "pineapple belongs on pizza", "expected_verdict": "opinion", "category": "opinion"},
    {"claim": "democracy is the best form of government", "expected_verdict": "opinion", "category": "opinion"},

    # Nuanced / contested (system should return "contested" or moderate verdicts)
    {"claim": "sugar is worse than fat for health", "expected_verdict": "contested", "category": "contested"},
    {"claim": "nuclear energy is safe", "expected_verdict": "contested", "category": "contested"},
    {"claim": "remote work is more productive than office work", "expected_verdict": "contested", "category": "contested"},

    # Current events / hard claims
    {"claim": "AI will replace most jobs", "expected_verdict": "contested", "category": "current_event"},
    {"claim": "the United States economy is in a recession", "expected_verdict": "contested", "category": "current_event"},

    # Bank claims (add 2-3 per phase)
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


# ── Pipeline Step Functions ──────────────────────────────────────────────────

API_FUNCTIONS = {
    "google_factcheck": search_factcheck,
    "wikipedia": search_wikipedia,
    "semantic_scholar": search_semantic_scholar,
    "open_alex": search_openalex,
    "duckduckgo": search_duckduckgo,
    "wikidata": search_wikidata,
}


def source_to_dict(source: Source) -> dict:
    return {
        "url": source.url,
        "title": source.title,
        "snippet": (source.snippet or "")[:300],
        "source_type": source.source_type,
        "raw_claim_rating": source.raw_claim_rating,
        "metadata": source.metadata,
    }


async def fetch_sources_by_api(request: ClaimRequest) -> dict[str, list[Source]]:
    """Call each API individually so we can tag which source came from where."""
    results = await asyncio.gather(
        *[fn(request) for fn in API_FUNCTIONS.values()],
        return_exceptions=True,
    )
    api_sources = {}
    for name, result in zip(API_FUNCTIONS.keys(), results):
        if isinstance(result, Exception):
            api_sources[name] = {"error": str(result), "sources": []}
        else:
            api_sources[name] = result
    return api_sources


def compute_relevance_scores(claim: str, sources: list[Source]) -> list[dict]:
    """Get relevance score for every source before filtering."""
    texts = []
    for source in sources:
        if source.title and source.snippet:
            text = f"{source.title}. {source.snippet}"
        else:
            text = source.title or source.snippet or ""
        texts.append(text)

    scores = compute_relevance(claim, texts)

    scored = []
    for source, text, score in zip(sources, texts, scores):
        is_non_content = _is_non_content(source.title)
        passes_threshold = score >= RELEVANCE_THRESHOLD
        kept = (not is_non_content) and (text == "" or passes_threshold)

        scored.append({
            "title": source.title,
            "url": source.url,
            "source_type": source.source_type,
            "relevance_score": round(float(score), 4),
            "is_non_content": is_non_content,
            "passes_threshold": passes_threshold,
            "kept": kept,
            "drop_reason": (
                "non_content_pattern" if is_non_content
                else f"relevance_{score:.3f}_below_{RELEVANCE_THRESHOLD}" if not passes_threshold and text != ""
                else None
            ),
        })
    return scored


def run_nli_on_source(source: Source, claim: str) -> dict:
    """Run NLI stance detection on a single source, capturing raw probabilities."""
    if source.source_type == "knowledge_graph":
        return {"method": "wikidata_skip", "reason": "structured_data_not_suited_for_nli"}
    if source.source_type == "fact_check" and source.raw_claim_rating:
        fc_stance, fc_conf = _stance_from_factcheck(source, claim)
        if fc_stance:
            return {
                "method": "factcheck_rating_bypass",
                "stance": fc_stance,
                "confidence": fc_conf,
                "raw_claim_rating": source.raw_claim_rating,
                "claim_reviewed": (source.metadata or {}).get("claim_reviewed", ""),
            }
        # Bypass failed: snippet is the false claim text, NLI on it would be wrong
        return {
            "method": "fc_skip",
            "reason": "bypass_failed_dropping",
            "raw_claim_rating": source.raw_claim_rating,
            "claim_reviewed": (source.metadata or {}).get("claim_reviewed", ""),
        }

    premise = source.snippet if source.snippet else source.title
    if not premise:
        return {"method": "skipped", "reason": "no_premise"}

    stance, confidence = classify_stance(premise, claim)
    return {
        "method": "nli_deberta",
        "premise_used": premise[:200],
        "stance": stance,
        "confidence": round(confidence, 4),
    }


async def run_full_pipeline(claim_data: dict) -> dict:
    """Run one claim through the entire pipeline, capturing every intermediate step."""
    claim_text = claim_data["claim"]
    request = ClaimRequest(claim=claim_text)
    result = {"claim": claim_text, "expected_verdict": claim_data["expected_verdict"], "category": claim_data["category"]}

    # Step 1: Claim type classification
    claim_type, ct_conf = classify_claim_type(claim_text)
    result["claim_type"] = {"type": claim_type, "confidence": round(ct_conf, 4)}

    # Step 2: Fetch sources per API
    api_sources = await fetch_sources_by_api(request)
    api_summary = {}
    all_sources = []
    all_sources_with_origin = []

    for api_name, sources in api_sources.items():
        if isinstance(sources, dict) and "error" in sources:
            api_summary[api_name] = {"count": 0, "error": sources["error"]}
            continue
        api_summary[api_name] = {"count": len(sources)}
        for s in sources:
            all_sources.append(s)
            all_sources_with_origin.append({"api": api_name, "source": s})

    result["source_collection"] = {
        "per_api": api_summary,
        "total_raw": len(all_sources),
    }

    # Step 3: Relevance scoring (BEFORE filtering, so we see everything)
    relevance_data = compute_relevance_scores(claim_text, all_sources)
    dropped_sources = [r for r in relevance_data if not r["kept"]]
    kept_sources_data = [r for r in relevance_data if r["kept"]]

    result["relevance_filter"] = {
        "threshold": RELEVANCE_THRESHOLD,
        "total_before": len(all_sources),
        "total_after": len(kept_sources_data),
        "dropped_count": len(dropped_sources),
        "dropped": dropped_sources,
        "kept": kept_sources_data,
    }

    # Reconstruct the filtered source list
    kept_urls_titles = {(r["url"], r["title"]) for r in kept_sources_data}
    filtered_sources = [
        s for s in all_sources if (s.url, s.title) in kept_urls_titles
    ]

    # Step 4: Deduplication
    before_dedup = len(filtered_sources)
    deduped_sources = _deduplicate_sources(filtered_sources)
    dedup_dropped = before_dedup - len(deduped_sources)

    result["deduplication"] = {
        "before": before_dedup,
        "after": len(deduped_sources),
        "dropped": dedup_dropped,
    }

    # Step 5: NLI + Credibility on each surviving source
    credibility_results = await score_all_sources(deduped_sources)
    analyzed = []

    for source, cred in zip(deduped_sources, credibility_results):
        nli_result = run_nli_on_source(source, claim_text)
        origin_api = "unknown"
        for item in all_sources_with_origin:
            if item["source"].url == source.url and item["source"].title == source.title:
                origin_api = item["api"]
                break

        entry = {
            "origin_api": origin_api,
            "title": source.title,
            "url": source.url,
            "snippet": (source.snippet or "")[:300],
            "source_type": source.source_type,
            "nli": nli_result,
            "credibility": {
                "tier": cred["credibility_tier"],
                "score": cred["credibility_score"],
                "bias_rating": cred["bias_rating"],
                "factual_reporting": cred["factual_reporting"],
            },
        }

        # Compute the weight this source contributes to the verdict
        stance = nli_result.get("stance")
        conf = nli_result.get("confidence", 0)
        if stance and stance != "neutral" and conf:
            weight = conf * cred["credibility_score"]
            entry["verdict_weight"] = round(weight, 4)
            entry["verdict_direction"] = stance
        else:
            entry["verdict_weight"] = 0
            entry["verdict_direction"] = "neutral (no contribution)"

        analyzed.append(entry)

    result["analyzed_sources"] = analyzed

    # Step 6: Compute verdict manually (mirrors compute_verdict logic)
    weighted_supporting = 0.0
    weighted_opposing = 0.0
    supporting_sources = []
    opposing_sources = []
    neutral_sources = []

    for entry in analyzed:
        stance = entry["nli"].get("stance")
        conf = entry["nli"].get("confidence", 0)
        cred_score = entry["credibility"]["score"]

        if not stance or stance == "neutral" or entry["nli"].get("method") in ("skipped", "fc_skip", "wikidata_skip"):
            neutral_sources.append(entry["title"])
            continue

        weight = conf * cred_score
        if stance == "supporting":
            weighted_supporting += weight
            supporting_sources.append({"title": entry["title"], "weight": round(weight, 4)})
        elif stance == "opposing":
            weighted_opposing += weight
            opposing_sources.append({"title": entry["title"], "weight": round(weight, 4)})

    total = weighted_supporting + weighted_opposing
    if total == 0:
        ratio = 0.5
        confidence = 0.0
        verdict = "insufficient evidence"
    else:
        ratio = weighted_supporting / total
        confidence = abs(ratio - 0.5) * 2

        if claim_type == "opinion":
            if ratio >= 0.60:
                verdict = "sources lean supporting"
            elif ratio > 0.40:
                verdict = "sources divided"
            else:
                verdict = "sources lean opposing"
        else:
            if ratio >= 0.80:
                verdict = "strongly supported"
            elif ratio >= 0.60:
                verdict = "likely supported"
            elif ratio > 0.40:
                verdict = "contested"
            elif ratio >= 0.20:
                verdict = "likely opposed"
            else:
                verdict = "strongly opposed"

    result["verdict_computation"] = {
        "weighted_supporting": round(weighted_supporting, 4),
        "weighted_opposing": round(weighted_opposing, 4),
        "total_weight": round(total, 4),
        "support_ratio": round(ratio, 4),
        "confidence": round(confidence, 4),
        "verdict": verdict,
        "supporting_sources": supporting_sources,
        "opposing_sources": opposing_sources,
        "neutral_count": len(neutral_sources),
        "neutral_sources": neutral_sources,
    }

    # Step 7: Grade it
    expected = claim_data["expected_verdict"]
    if expected == "opinion":
        correct = verdict in ("sources lean supporting", "sources lean opposing", "sources divided")
    elif expected == "contested":
        correct = verdict in ("contested", "sources divided", "likely supported", "likely opposed")
    elif expected == "strongly supported":
        correct = verdict in ("strongly supported", "likely supported")
    elif expected == "strongly opposed":
        correct = verdict in ("strongly opposed", "likely opposed")
    else:
        correct = verdict == expected

    result["grade"] = {
        "expected": expected,
        "actual_verdict": verdict,
        "correct": correct,
    }

    return result


# ── Markdown Report Generator ────────────────────────────────────────────────

def generate_markdown(all_results: list[dict]) -> str:
    lines = []
    lines.append("# Baseline Test Report")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"Model: DeBERTa-v3-base-mnli-fever-anli (NLI) + XLM-R (claim type) + MiniLM (relevance)")
    lines.append(f"Relevance threshold: {RELEVANCE_THRESHOLD}")
    lines.append("")

    correct = sum(1 for r in all_results if r["grade"]["correct"])
    total = len(all_results)
    lines.append(f"## Summary: {correct}/{total} correct")
    lines.append("")

    by_category = {}
    for r in all_results:
        cat = r["category"]
        if cat not in by_category:
            by_category[cat] = {"correct": 0, "total": 0}
        by_category[cat]["total"] += 1
        if r["grade"]["correct"]:
            by_category[cat]["correct"] += 1

    lines.append("| Category | Score |")
    lines.append("|----------|-------|")
    for cat, stats in by_category.items():
        emoji = "PASS" if stats["correct"] == stats["total"] else "FAIL"
        lines.append(f"| {cat} | {stats['correct']}/{stats['total']} {emoji} |")
    lines.append("")

    lines.append("| Claim | Expected | Actual | Match |")
    lines.append("|-------|----------|--------|-------|")
    for r in all_results:
        match = "YES" if r["grade"]["correct"] else "**NO**"
        lines.append(f"| {r['claim']} | {r['grade']['expected']} | {r['grade']['actual_verdict']} | {match} |")
    lines.append("")

    for i, r in enumerate(all_results, 1):
        lines.append(f"---")
        lines.append(f"## {i}. \"{r['claim']}\"")
        lines.append(f"Category: {r['category']}")
        lines.append(f"Expected: {r['grade']['expected']}")
        grade_marker = "YES" if r["grade"]["correct"] else "**NO - MISMATCH**"
        lines.append(f"Actual: {r['grade']['actual_verdict']} ({grade_marker})")
        lines.append(f"Claim type: {r['claim_type']['type']} ({r['claim_type']['confidence']})")
        lines.append("")

        sc = r["source_collection"]
        lines.append(f"### Sources collected: {sc['total_raw']} total")
        for api, info in sc["per_api"].items():
            if "error" in info:
                lines.append(f"  - {api}: ERROR - {info['error']}")
            else:
                lines.append(f"  - {api}: {info['count']}")
        lines.append("")

        rf = r["relevance_filter"]
        lines.append(f"### Relevance filter: {rf['total_before']} -> {rf['total_after']} (dropped {rf['dropped_count']})")
        if rf["dropped"]:
            lines.append("Dropped sources:")
            for d in rf["dropped"]:
                lines.append(f"  - [{d['source_type']}] \"{d['title']}\" (relevance: {d['relevance_score']}, reason: {d['drop_reason']})")
        lines.append("")

        dd = r["deduplication"]
        lines.append(f"### Dedup: {dd['before']} -> {dd['after']} (dropped {dd['dropped']})")
        lines.append("")

        lines.append(f"### Analyzed sources ({len(r['analyzed_sources'])} total)")
        lines.append("")

        for entry in r["analyzed_sources"]:
            stance = entry["nli"].get("stance", "N/A")
            conf = entry["nli"].get("confidence", 0)
            method = entry["nli"].get("method", "N/A")
            cred = entry["credibility"]

            stance_display = f"{stance} ({conf})" if conf else stance
            lines.append(f"**[{entry['origin_api']}] \"{entry['title']}\"**")
            lines.append(f"  Type: {entry['source_type']} | Cred: {cred['tier']} {cred['score']}" +
                         (f" | Bias: {cred['bias_rating']}" if cred['bias_rating'] else "") +
                         (f" | Factual: {cred['factual_reporting']}" if cred['factual_reporting'] else ""))
            lines.append(f"  NLI ({method}): {stance_display}")
            lines.append(f"  Verdict contribution: {entry['verdict_direction']} (weight: {entry['verdict_weight']})")
            lines.append(f"  Snippet: \"{entry['snippet'][:150]}...\"")
            lines.append("")

        vc = r["verdict_computation"]
        lines.append(f"### Verdict computation")
        lines.append(f"  Supporting weight: {vc['weighted_supporting']}")
        lines.append(f"  Opposing weight: {vc['weighted_opposing']}")
        lines.append(f"  Support ratio: {vc['support_ratio']}")
        lines.append(f"  Confidence: {vc['confidence']}")
        lines.append(f"  Verdict: **{vc['verdict']}**")
        lines.append(f"  Neutral sources (no contribution): {vc['neutral_count']}")
        lines.append("")

        if vc["supporting_sources"]:
            lines.append("  Top supporting:")
            for s in sorted(vc["supporting_sources"], key=lambda x: -x["weight"])[:5]:
                lines.append(f"    - {s['title']} (weight: {s['weight']})")
        if vc["opposing_sources"]:
            lines.append("  Top opposing:")
            for s in sorted(vc["opposing_sources"], key=lambda x: -x["weight"])[:5]:
                lines.append(f"    - {s['title']} (weight: {s['weight']})")
        lines.append("")

    return "\n".join(lines)


# ── Main ─────────────────────────────────────────────────────────────────────

async def main():
    os.makedirs("tests", exist_ok=True)

    print(f"Running baseline test on {len(TEST_CLAIMS)} claims...")
    print(f"This will take a few minutes (API calls + NLI inference per claim).\n")

    all_results = []
    for i, claim_data in enumerate(TEST_CLAIMS, 1):
        print(f"[{i}/{len(TEST_CLAIMS)}] Testing: \"{claim_data['claim']}\"")
        try:
            result = await run_full_pipeline(claim_data)
            verdict = result["verdict_computation"]["verdict"]
            correct = result["grade"]["correct"]
            marker = "PASS" if correct else "FAIL"
            print(f"  -> {verdict} (expected: {claim_data['expected_verdict']}) [{marker}]\n")
            all_results.append(result)
        except Exception as e:
            print(f"  -> ERROR: {e}\n")
            all_results.append({
                "claim": claim_data["claim"],
                "category": claim_data["category"],
                "error": str(e),
                "grade": {"expected": claim_data["expected_verdict"], "actual_verdict": "error", "correct": False},
            })

    # Save JSON
    json_path = "tests/baseline_results.json"
    with open(json_path, "w") as f:
        json.dump(all_results, f, indent=2, default=str)
    print(f"JSON saved: {json_path}")

    # Save markdown report
    md_path = "tests/baseline_report.md"
    with open(md_path, "w") as f:
        f.write(generate_markdown(all_results))
    print(f"Markdown report saved: {md_path}")

    # Print summary
    correct = sum(1 for r in all_results if r["grade"]["correct"])
    print(f"\n{'='*60}")
    print(f"BASELINE SCORE: {correct}/{len(all_results)}")
    print(f"{'='*60}")

    for r in all_results:
        marker = "PASS" if r["grade"]["correct"] else "FAIL"
        actual = r.get("verdict_computation", {}).get("verdict", r.get("error", "?"))
        print(f"  [{marker}] {r['claim']}: {actual} (expected: {r['grade']['expected']})")


if __name__ == "__main__":
    asyncio.run(main())