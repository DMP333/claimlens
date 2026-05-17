import asyncio
import heapq
from app.models.schemas import ClaimRequest, SourceResult, ClaimResponse, Source
from app.services.google_factcheck import search_factcheck
from app.services.wikipedia import search_wikipedia
from app.services.semantic_scholar import search_semantic_scholar
from app.services.open_alex import search_openalex
from app.services.duckduckgo import search_duckduckgo
from app.services.wikidata import search_wikidata


async def analyze_claim(request: ClaimRequest) -> ClaimResponse:
    raw_sources = await search_sources(request)
    analyzed_sources = analyze_sources(request.claim, raw_sources)
    verdict, confidence_in_verdict = compute_verdict(analyzed_sources)
    return ClaimResponse(
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


def analyze_sources(claim: str, raw_sources: list[Source]) -> list[SourceResult]:
    #TODO: implement NLI stance detection
    results = []
    for source in raw_sources:
        results.append(
            SourceResult(
                url=source.url,
                title=source.title,
                stance="opposing",
                reliability=0.85,
                support_summary="Placeholder analysis.",
            )
        )
    return results


def compute_verdict(source_results_list: list[SourceResult]) -> tuple[str, float]:
    #TODO: implement real verdict logic with NLI integration
    return ("inconclusive", 0.0)