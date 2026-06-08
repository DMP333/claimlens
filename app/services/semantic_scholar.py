import httpx
import asyncio
from app.models.schemas import Source
from app.models.schemas import ClaimRequest
from app.core.config import settings

SEMANTIC_URL = "https://api.semanticscholar.org/graph/v1/paper/search"


async def search_semantic_scholar(
    claim_request: ClaimRequest,
    source_config: dict | None = None,
) -> list[Source]:
    """Search Semantic Scholar for academic papers.

    Args:
        claim_request: the claim to search for
        source_config: optional routing config with keys:
            - max_results (int): how many results to fetch
            - field_filters (list[str] | None): academic fields to filter by
              e.g. ["Biology", "Medicine"]
    """
    cfg = source_config or {}
    max_results = cfg.get("max_results", 10)
    field_filters = cfg.get("field_filters")

    headers = {"x-api-key": settings.SEMANTIC_SCHOLAR_API_KEY}
    params = {
        "query": claim_request.claim,
        "limit": max_results,
        "fields": "title,abstract,url,year,citationCount,fieldsOfStudy",
    }

    # Apply field-of-study filter at query level
    if field_filters:
        params["fieldsOfStudy"] = ",".join(field_filters)
        print(f"[SS] Field filter: {field_filters}")

    async with httpx.AsyncClient() as client:
        response = await client.get(SEMANTIC_URL, params=params, headers=headers)

        if response.status_code == 429:
            await asyncio.sleep(1)
            response = await client.get(SEMANTIC_URL, params=params, headers=headers)

    if response.status_code != 200:
        return []

    data = response.json()
    results = data.get("data", [])

    sources = []
    for item in results:
        fields_of_study = item.get("fieldsOfStudy") or []

        source = Source(
            url=item.get("url", ""),
            title=item.get("title", ""),
            snippet=item.get("abstract") or item.get("title") or "",
            source_type="academic",
            raw_claim_rating=None,
            metadata={
                "citation_count": item.get("citationCount", 0),
                "fields_of_study": fields_of_study,
            },
        )
        sources.append(source)

    if field_filters:
        print(f"[SS] {len(results)} results (filtered to {', '.join(field_filters)})")
    else:
        print(f"[SS] {len(results)} results (no field filter)")

    return sources