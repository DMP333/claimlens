import httpx
from app.models.schemas import Source, ClaimRequest

OPENALEX_URL = "https://api.openalex.org/works"

#TODO: explore different parameter options for api
async def search_openalex(claim_request: ClaimRequest) -> list[Source]:
    params = {
        "search": claim_request.claim,
        "per_page": 10,
        "filter": f"publication_year:{claim_request.date_range_start.year}-{claim_request.date_range_end.year}",
        "sort": "relevance_score:desc",
        "select": "id,display_name,doi,abstract_inverted_index,publication_year,cited_by_count",
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(OPENALEX_URL, params=params)

    if response.status_code != 200:
        return []

    data = response.json()
    results = data.get("results", [])

    sources = []
    for item in results:
        abstract_index = item.get("abstract_inverted_index")
        snippet = _reconstruct_abstract(abstract_index) if abstract_index else item.get("display_name", "")

        doi = item.get("doi", "")
        openalex_id = item.get("id", "").split("/")[-1]
        url = doi if doi else f"https://openalex.org/works/{openalex_id}"

        source = Source(
            url=url,
            title=item.get("display_name", ""),
            snippet=snippet,
            source_type="academic",
            raw_claim_rating=None,
            metadata={"citation_count": item.get("cited_by_count", 0)},
        )
        sources.append(source)

    return sources


def _reconstruct_abstract(inverted_index: dict) -> str:
    word_positions = []
    for word, positions in inverted_index.items():
        for pos in positions:
            word_positions.append((pos, word))
    word_positions.sort()
    return " ".join(word for _, word in word_positions)