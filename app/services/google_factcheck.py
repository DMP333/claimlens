import asyncio
import httpx
import trafilatura
from app.models.schemas import Source, ClaimRequest
from app.core.config import settings
from app.services.content_extractor import extract_relevant_paragraphs

FACTCHECK_URL = "https://factchecktools.googleapis.com/v1alpha1/claims:search"
FETCH_TIMEOUT = 4.0
MIN_ENRICHED_WORDS = 30


async def search_factcheck(claim_request: ClaimRequest) -> list[Source]:
    params = {
        "query": claim_request.claim,
        "key": settings.GOOGLE_FACTCHECK_API_KEY,
        "languageCode": "en",
        "pageSize": 10
    }

    async with httpx.AsyncClient(
        timeout=FETCH_TIMEOUT,
        follow_redirects=True,
        headers={"User-Agent": "Mozilla/5.0 (compatible; ClaimVerifier/1.0)"},
    ) as client:

        # Step 1: Query the FC API
        response = await client.get(FACTCHECK_URL, params=params)
        if response.status_code != 200:
            return []

        data = response.json()
        claims = data.get("claims", [])

        # Step 2: Expand ALL claimReviews into separate sources
        # Previously we only took claimReview[0], missing independent
        # reviews from other fact-checkers on the same claim.
        sources = []
        urls_to_fetch = []

        for item in claims:
            claim_text = item.get("text", "")
            claimant = item.get("claimant", "")
            claim_date = item.get("claimDate", "")
            reviews = item.get("claimReview", [])

            if not reviews:
                continue

            for review in reviews:
                publisher = review.get("publisher", {})
                article_url = review.get("url", "")

                source = Source(
                    url=article_url,
                    title=review.get("title", claim_text),
                    snippet=claim_text,  # placeholder, replaced after article fetch
                    source_type="fact_check",
                    raw_claim_rating=review.get("textualRating", None),
                    metadata={
                        "claim_reviewed": claim_text,
                        "claimant": claimant,
                        "claim_date": claim_date,
                        "review_date": review.get("reviewDate", ""),
                        "publisher_name": publisher.get("name", ""),
                        "publisher_site": publisher.get("site", ""),
                    },
                )
                sources.append(source)
                urls_to_fetch.append(article_url)

        review_count = len(sources)
        claim_count = len(claims)
        if review_count > claim_count:
            print(f"[FC] {claim_count} claims expanded to {review_count} sources (multiple reviews found)")
        else:
            print(f"[FC] {claim_count} claims, {review_count} sources")

        # Step 3: Fetch all article URLs in parallel
        fetched_texts = await _fetch_all(client, urls_to_fetch)

        # Step 4: Enrich sources with extracted evidence
        enriched_count = 0
        for source, fetched in zip(sources, fetched_texts):
            if fetched and len(fetched.split()) >= MIN_ENRICHED_WORDS:
                evidence, extract_score = extract_relevant_paragraphs(
                    fetched, claim_request.claim
                )
                if evidence and len(evidence.split()) >= MIN_ENRICHED_WORDS:
                    source.snippet = evidence
                    source.metadata["enriched"] = True
                    source.metadata["extract_score"] = extract_score
                    enriched_count += 1
                    continue

            # Fetch failed or too short: keep original claim text as snippet
            source.metadata["enriched"] = False
            source.metadata["extract_score"] = None

        print(f"[FC] {enriched_count}/{review_count} enriched with article evidence")

    return sources


async def _fetch_all(
    client: httpx.AsyncClient, urls: list[str]
) -> list[str]:
    """Fetch multiple fact-check article pages in parallel."""
    tasks = [_fetch_article_text(client, url) for url in urls]
    results = await asyncio.gather(*tasks, return_exceptions=True)
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
        result = trafilatura.extract(response.text)
        return result or ""
    except Exception:
        return ""