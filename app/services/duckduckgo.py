import asyncio
import httpx
from ddgs import DDGS
from app.models.schemas import Source, ClaimRequest
from app.services.content_extractor import extract_relevant_paragraphs


FETCH_TIMEOUT = 3.0   # max seconds per URL fetch
MIN_ENRICHED_WORDS = 25  # below this, fall back to DDG snippet


async def search_duckduckgo(claim_request: ClaimRequest) -> list[Source]:
    # Step 1: DDG search for URLs + preview snippets (same as before)
    def _search():
        with DDGS() as ddgs:
            return list(ddgs.text(claim_request.claim, max_results=10))

    results = await asyncio.to_thread(_search)

    # Step 2: Fetch actual page content in parallel
    urls = [item.get("href", "") for item in results]
    fetched_texts = await _fetch_all(urls)

    # Step 3: Build sources with evidence-extracted snippets
    sources = []
    for item, fetched in zip(results, fetched_texts):
        ddg_snippet = item.get("body", "")

        # Use fetched article text if good enough, otherwise keep DDG snippet
        if fetched and len(fetched.split()) >= MIN_ENRICHED_WORDS:
            snippet, extract_score = extract_relevant_paragraphs(fetched, claim_request.claim)
            enriched = True
        else:
            snippet = ddg_snippet
            extract_score = None
            enriched = False

        source = Source(
            url=item.get("href", ""),
            title=item.get("title", ""),
            snippet=snippet,
            source_type="web",
            raw_claim_rating=None,
            metadata={"ddg_snippet": ddg_snippet, "enriched": enriched,
                       "extract_score": extract_score},
        )
        sources.append(source)

    enriched_count = sum(1 for item, f in zip(results, fetched_texts)
                        if f and len(f.split()) >= MIN_ENRICHED_WORDS)
    print(f"[DDG] {len(results)} results, {enriched_count} enriched with full article text")

    return sources


async def _fetch_all(urls: list[str]) -> list[str]:
    """Fetch multiple URLs in parallel with timeout."""
    async with httpx.AsyncClient(
        timeout=FETCH_TIMEOUT,
        follow_redirects=True,
        headers={"User-Agent": "Mozilla/5.0 (compatible; ClaimVerifier/1.0)"},
    ) as client:
        tasks = [_fetch_article_text(client, url) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)

    # Convert exceptions to empty strings
    return [r if isinstance(r, str) else "" for r in results]


async def _fetch_article_text(client: httpx.AsyncClient, url: str) -> str:
    """Fetch a URL and extract article text from HTML."""
    if not url:
        return ""

    try:
        response = await client.get(url)
        if response.status_code != 200:
            return ""

        content_type = response.headers.get("content-type", "")
        if "text/html" not in content_type.lower():
            return ""

        return _extract_text_from_html(response.text)
    except Exception:
        return ""


def _extract_text_from_html(html: str) -> str:
    """Extract article text from HTML using trafilatura.

    trafilatura is specifically designed for article extraction,
    handling navigation, ads, sidebars, and HTML entities correctly.
    Returns the full extracted text (paragraph extraction happens later).
    """
    import trafilatura
    result = trafilatura.extract(html)
    return result or ""