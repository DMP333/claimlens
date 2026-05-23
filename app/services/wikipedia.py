import httpx #http library import
from app.models.schemas import Source #to return defined Source object we have defined
import re #regular expressions for stripping HTML tags from snippets
from app.models.schemas import ClaimRequest

WIKI_URL = "https://en.wikipedia.org/w/api.php" #endpoint url, defined outside of function as it is never gonna change

#TODO: explore different parameter option for api
async def search_wikipedia(claim_request: ClaimRequest) -> list[Source]:
    params = {
        "action": "query",
        "list": "search",
        "srsearch": claim_request.claim,
        "format": "json",
        "srlimit": 10,
    }

    headers = {"User-Agent": "FalseClaimDetector/1.0 (minwoopark.333@gmail.com)"}

    async with httpx.AsyncClient() as client:
        response = await client.get(WIKI_URL, params=params, headers=headers)

        if response.status_code != 200:
            return []

        data = response.json()
        results = data.get("query", {}).get("search", [])

        sources = []
        titles = []
        for item in results:
            title = item.get("title", "")
            titles.append(title)
            source = Source(
                url=f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}",
                title=title,
                snippet=item.get("snippet", ""),
                source_type="encyclopedia",
                raw_claim_rating=None,
                metadata={},
            )
            sources.append(source)

        if not titles:
            return sources

        # Second call: fetch article length, quality categories, and intro paragraph
        quality_params = {
            "action": "query",
            "titles": "|".join(titles[:10]),
            "prop": "info|categories|extracts",
            "cllimit": "50",
            "clcategories": "Category:Featured articles|Category:Good articles",
            "exintro": True,        # only the intro section, not full article
            "explaintext": True,    # plain text, not HTML
            "exsentences": 5,       # first 5 sentences of intro
            "format": "json",
        }
        quality_response = await client.get(WIKI_URL, params=quality_params, headers=headers)

        if quality_response.status_code != 200:
            return sources

        pages = quality_response.json().get("query", {}).get("pages", {})
        quality_map = {}
        for page_id, page_data in pages.items():
            title = page_data.get("title", "")
            length = page_data.get("length", 0)
            extract = page_data.get("extract", "")
            categories = [c.get("title", "") for c in page_data.get("categories", [])]
            is_featured = "Category:Featured articles" in categories
            is_good = "Category:Good articles" in categories
            quality_map[title] = {
                "article_length": length,
                "is_featured": is_featured,
                "is_good": is_good,
                "extract": extract,
            }

        for source in sources:
            if source.title in quality_map:
                source.metadata = quality_map[source.title]
                # Replace search snippet with actual article intro for better NLI classification
                # Search snippets are noisy fragments; intro paragraphs contain the article's actual stance
                if quality_map[source.title].get("extract"):
                    source.snippet = quality_map[source.title]["extract"]

    return sources