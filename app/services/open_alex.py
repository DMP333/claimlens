import httpx
from app.models.schemas import Source, ClaimRequest

OPENALEX_URL = "https://api.openalex.org/works"

# Map our Semantic Scholar field names to OpenAlex domain names
# OpenAlex has 4 domains: Life Sciences, Physical Sciences,
# Social Sciences, Health Sciences
_FIELD_TO_DOMAIN = {
    "Biology": {"Life Sciences"},
    "Medicine": {"Health Sciences", "Life Sciences"},
    "Physics": {"Physical Sciences"},
    "Chemistry": {"Physical Sciences"},
    "Environmental Science": {"Life Sciences", "Physical Sciences"},
    "Psychology": {"Social Sciences", "Health Sciences"},
    "Economics": {"Social Sciences"},
    "Political Science": {"Social Sciences"},
    "History": {"Social Sciences"},
}


def _get_expected_domains(field_filters: list[str]) -> set[str]:
    """Convert SS-style field filters to OpenAlex domain names."""
    domains = set()
    for field in field_filters:
        domains.update(_FIELD_TO_DOMAIN.get(field, set()))
    return domains


async def search_openalex(
    claim_request: ClaimRequest,
    source_config: dict | None = None,
) -> list[Source]:
    """Search OpenAlex for academic papers.

    Args:
        claim_request: the claim to search for
        source_config: optional routing config with keys:
            - max_results (int): how many results to fetch
            - field_filters (list[str] | None): SS-style field names for
              post-retrieval domain filtering
    """
    cfg = source_config or {}
    max_results = cfg.get("max_results", 10)
    field_filters = cfg.get("field_filters")

    params = {
        "search": claim_request.claim,
        "per_page": max_results,
        "filter": f"publication_year:{claim_request.date_range_start.year}-{claim_request.date_range_end.year}",
        "sort": "relevance_score:desc",
        "select": "id,display_name,doi,abstract_inverted_index,publication_year,cited_by_count,primary_topic",
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(OPENALEX_URL, params=params)

    if response.status_code != 200:
        return []

    data = response.json()
    results = data.get("results", [])

    # Determine expected domains for post-retrieval filtering
    expected_domains = _get_expected_domains(field_filters) if field_filters else None

    sources = []
    filtered_count = 0
    for item in results:
        abstract_index = item.get("abstract_inverted_index")
        snippet = _reconstruct_abstract(abstract_index) if abstract_index else item.get("display_name", "")

        doi = item.get("doi", "")
        openalex_id = item.get("id", "").split("/")[-1]
        url = doi if doi else f"https://openalex.org/works/{openalex_id}"

        # Extract topic information
        primary_topic = item.get("primary_topic") or {}
        topic_domain = primary_topic.get("domain", {}).get("display_name", "")
        topic_field = primary_topic.get("field", {}).get("display_name", "")
        topic_subfield = primary_topic.get("subfield", {}).get("display_name", "")

        # Post-retrieval domain filtering
        if expected_domains and topic_domain and topic_domain not in expected_domains:
            print(f"[OA-FILTER] Dropped: '{item.get('display_name', '')[:60]}' (domain: {topic_domain}, expected: {expected_domains})")
            filtered_count += 1
            continue

        source = Source(
            url=url,
            title=item.get("display_name", ""),
            snippet=snippet,
            source_type="academic",
            raw_claim_rating=None,
            metadata={
                "citation_count": item.get("cited_by_count", 0),
                "topic_domain": topic_domain,
                "topic_field": topic_field,
                "topic_subfield": topic_subfield,
            },
        )
        sources.append(source)

    if field_filters:
        print(f"[OA] {len(results)} results, {filtered_count} filtered by domain, {len(sources)} kept (fields: {field_filters})")
    else:
        print(f"[OA] {len(results)} results (no field filter)")

    return sources


def _reconstruct_abstract(inverted_index: dict) -> str:
    word_positions = []
    for word, positions in inverted_index.items():
        for pos in positions:
            word_positions.append((pos, word))
    word_positions.sort()
    return " ".join(word for _, word in word_positions)