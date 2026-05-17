import asyncio
from ddgs import DDGS
from app.models.schemas import Source, ClaimRequest

#TODO: explore different parameter options for api
async def search_duckduckgo(claim_request: ClaimRequest) -> list[Source]:
    def _search():
        with DDGS() as ddgs:
            return list(ddgs.text(claim_request.claim, max_results=10))

    results = await asyncio.to_thread(_search)

    sources = []
    for item in results:
        source = Source(
            url=item.get("href", ""),
            title=item.get("title", ""),
            snippet=item.get("body", ""),
            source_type="web",
            raw_claim_rating=None,
        )
        sources.append(source)

    return sources