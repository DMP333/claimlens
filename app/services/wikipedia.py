import asyncio
import httpx
import re
from app.models.schemas import Source, ClaimRequest
from app.services.content_extractor import extract_relevant_paragraphs

WIKI_API_URL = "https://en.wikipedia.org/w/api.php"
WIKI_HEADERS = {"User-Agent": "FalseClaimDetector/1.0 (minwoopark.333@gmail.com)"}
FETCH_TIMEOUT = 4.0   # slightly longer than DDG since Wikipedia is reliable
MIN_ENRICHED_WORDS = 30


async def search_wikipedia(claim_request: ClaimRequest) -> list[Source]:
    claim = claim_request.claim

    async with httpx.AsyncClient(
        timeout=FETCH_TIMEOUT,
        follow_redirects=True,
        headers=WIKI_HEADERS,
    ) as client:

        # Step 1: Search for relevant article titles
        search_params = {
            "action": "query",
            "list": "search",
            "srsearch": claim,
            "format": "json",
            "srlimit": 5,
        }
        response = await client.get(WIKI_API_URL, params=search_params)
        if response.status_code != 200:
            return []

        results = response.json().get("query", {}).get("search", [])
        if not results:
            return []

        titles = [item.get("title", "") for item in results]

        # Step 2: Fetch article metadata + intro text (fallback)
        meta_params = {
            "action": "query",
            "titles": "|".join(titles[:5]),
            "prop": "info|categories|extracts",
            "cllimit": "50",
            "clcategories": "Category:Featured articles|Category:Good articles",
            "exintro": True,
            "explaintext": True,
            "exsentences": 5,
            "format": "json",
        }
        meta_response = await client.get(WIKI_API_URL, params=meta_params)

        quality_map = {}
        if meta_response.status_code == 200:
            pages = meta_response.json().get("query", {}).get("pages", {})
            for page_id, page_data in pages.items():
                title = page_data.get("title", "")
                categories = [c.get("title", "") for c in page_data.get("categories", [])]
                quality_map[title] = {
                    "article_length": page_data.get("length", 0),
                    "is_featured": "Category:Featured articles" in categories,
                    "is_good": "Category:Good articles" in categories,
                    "intro_extract": page_data.get("extract", ""),
                }

        # Step 3: Fetch full page text in parallel
        urls = [
            f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}"
            for title in titles
        ]
        fetched_texts = await _fetch_all(client, urls)

        # Step 4: Build sources with extracted evidence paragraphs
        sources = []
        enriched_count = 0
        for item, title, fetched in zip(results, titles, fetched_texts):
            url = f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}"
            meta = quality_map.get(title, {})
            intro_extract = meta.get("intro_extract", "")

            # Use full article text with content_extractor if available
            if fetched and len(fetched.split()) >= MIN_ENRICHED_WORDS:
                snippet, extract_score = extract_relevant_paragraphs(fetched, claim)
                enriched = True
                enriched_count += 1
            elif intro_extract:
                # Fallback: use 5-sentence intro from API
                snippet = intro_extract
                extract_score = None
                enriched = False
            else:
                # Last resort: use search snippet
                snippet = item.get("snippet", "")
                snippet = re.sub(r'<[^>]+>', '', snippet)  # strip HTML tags
                extract_score = None
                enriched = False

            meta["enriched"] = enriched
            meta["extract_score"] = extract_score

            source = Source(
                url=url,
                title=title,
                snippet=snippet,
                source_type="encyclopedia",
                raw_claim_rating=None,
                metadata=meta,
            )
            sources.append(source)

        print(f"[WIKI] {len(results)} results, {enriched_count} enriched with full article text")

    return sources


async def _fetch_all(client: httpx.AsyncClient, urls: list[str]) -> list[str]:
    """Fetch multiple Wikipedia pages in parallel."""
    tasks = [_fetch_page_text(client, url) for url in urls]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    return [r if isinstance(r, str) else "" for r in results]


async def _fetch_page_text(client: httpx.AsyncClient, url: str) -> str:
    """Fetch a Wikipedia page and extract article text."""
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
    """Extract article text from Wikipedia HTML using trafilatura."""
    import trafilatura
    result = trafilatura.extract(html)
    return result or ""