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
        "srlimit": 10
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(WIKI_URL, params=params)

    if response.status_code != 200:
        return []

    data = response.json()
    results = data.get("query", {}).get("search", [])

    sources = []
    for item in results:
        title = item.get("title", "")
        raw_snippet = item.get("snippet", "")
        clean_snippet = re.sub(r"<[^>]+>", "", raw_snippet) #strips all html tag

        source = Source(
            url=f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}",
            title=title,
            snippet=clean_snippet,
            source_type="encyclopedia",
            raw_claim_rating=None
        )
        sources.append(source)

    return sources