import asyncio
import heapq
from app.models.schemas import ClaimRequest, SourceResult, ClaimResponse, Source
from app.services.google_factcheck import search_factcheck
from app.services.wikipedia import search_wikipedia
from app.services.semantic_scholar import search_semantic_scholar
from app.services.open_alex import search_openalex
from app.services.duckduckgo import search_duckduckgo
from app.services.wikidata import search_wikidata
from app.services.nli_service import classify_stance
from app.services.credibility_service import score_all_sources


async def analyze_claim(request: ClaimRequest) -> ClaimResponse:
    from app.services.nli_service import classify_claim_type

    claim_type, claim_type_confidence = classify_claim_type(request.claim)
    raw_sources = await search_sources(request)
    analyzed_sources = await analyze_sources(request.claim, raw_sources)
    verdict, confidence_in_verdict = compute_verdict(analyzed_sources, claim_type)
    return ClaimResponse(
        claim=request.claim,
        claim_type=claim_type,
        claim_type_confidence=claim_type_confidence,
        verdict=verdict,
        confidence_in_verdict=confidence_in_verdict,
        sources=analyzed_sources,
    )

async def search_sources(request: ClaimRequest) -> list[Source]:
    service_names = [
        "google_factcheck",
        "wikipedia",
        "semantic_scholar",
        "open_alex",
        "duckduckgo",
        "wikidata",
    ]

    results = await asyncio.gather(
        search_factcheck(request),
        search_wikipedia(request),
        search_semantic_scholar(request),
        search_openalex(request),
        search_duckduckgo(request),
        search_wikidata(request),
        return_exceptions=True,
    )

    all_sources = []
    for name, result in zip(service_names, results):
        if isinstance(result, Exception):
            print(f"[ERROR] {name}: {result}")
        else:
            print(f"[OK] {name}: {len(result)} sources")
            all_sources.extend(result)

    return all_sources

async def analyze_sources(claim: str, raw_sources: list[Source]) -> list[SourceResult]:
    credibility_results = await score_all_sources(raw_sources)

    results = []
    for source, cred in zip(raw_sources, credibility_results):
        if not source.snippet:
            continue

        premise = f"{source.title}. {source.snippet}" if source.title else source.snippet
        stance, confidence = classify_stance(premise, claim)

        results.append(
            SourceResult(
                url=source.url,
                title=source.title,
                stance=stance,
                stance_confidence=confidence,
                credibility_tier=cred["credibility_tier"],
                credibility_score=cred["credibility_score"],
                bias_rating=cred["bias_rating"],
                factual_reporting=cred["factual_reporting"],
                support_summary=f"NLI: {stance} ({confidence:.2f})",
            )
        )
    return results

def compute_verdict(source_results_list: list[SourceResult], claim_type: str) -> tuple[str, float]:
    weighted_supporting = 0.0
    weighted_opposing = 0.0

    for source in source_results_list:
        if source.stance == "neutral":
            continue
        weight = source.stance_confidence * source.credibility_score
        if source.stance == "supporting":
            weighted_supporting += weight
        elif source.stance == "opposing":
            weighted_opposing += weight

    total = weighted_supporting + weighted_opposing

    if total == 0:
        return ("insufficient evidence", 0.0)

    ratio = weighted_supporting / total
    confidence = abs(ratio - 0.5) * 2

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

    return (verdict, round(confidence, 4))