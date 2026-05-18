import httpx #http library import
import asyncio
from app.models.schemas import Source #to return defined Source object we have defined
from app.models.schemas import ClaimRequest
from app.core.config import settings #setting that we had, what allows google api to access it without following direc code

SEMANTIC_URL = "https://api.semanticscholar.org/graph/v1/paper/search" #endpoint url, defined outside of function as it is never gonna change

#TODO: explore different parameter option for api
async def search_semantic_scholar(claim_request: ClaimRequest) -> list[Source]:
    headers = {"x-api-key": settings.SEMANTIC_SCHOLAR_API_KEY}
    params = {
        "query": claim_request.claim,
        "limit": 10,
        "year": f"{claim_request.date_range_start.year}-{claim_request.date_range_end.year}",
        "fields": "title,abstract,url,year,citationCount"
    }

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
        source = Source(
            url=item.get("url", ""),
            title=item.get("title", ""),
            snippet=item.get("abstract") or item.get("title") or "",
            source_type="academic",
            raw_claim_rating=None,
            metadata={"citation_count": item.get("citationCount", 0)},
        )
        sources.append(source)

    return sources