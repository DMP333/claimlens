import httpx #http library import
from app.core.config import settings #setting that we had, what allows google api to access it without following direc code
from app.models.schemas import Source #to return defined Source object we have defined
from app.models.schemas import ClaimRequest

FACTCHECK_URL = "https://factchecktools.googleapis.com/v1alpha1/claims:search" #endpoint ur, defined outside of function as it is never gonna change

#TODO: explore differnt parameter option for api
async def search_factcheck(claim_request: ClaimRequest) -> list[Source]:
    #this function will not block other functions from running, in case we wait for https, this will not affect other functions
    #we do not need multithreading here cuz all we are doing is waiting for the response, api are doing most of the work, not me
    #all we are doing is processing after receiving the response from the api call, which barely takes any time
    params = { #what gets appeneded into the url, each of them match the parameter defined by the google api
        "query": claim_request.claim,
        "key": settings.GOOGLE_FACTCHECK_API_KEY,
        "languageCode": "en", #filters the result
        "pageSize": 10
    }

    async with httpx.AsyncClient() as client: #creates an http client, async means once we get what we need automatically clean this cleint up
        response = await client.get(FACTCHECK_URL, params=params) #actual network call, awaits make sure we wait till this task is complete before executing rest of the funciton

    if response.status_code != 200: #if google shoots the error, we return empty list instead of crashing the code
        return []

    data = response.json() #google returns the json file so we turn this into dictionary
    claims = data.get("claims", []) #accessing claims dictionary

    sources = []
    for item in claims:
        review = item.get("claimReview", [{}])[0]
        source = Source(
            url=review.get("url", ""),
            title=review.get("title", item.get("text", "")),
            snippet=item.get("text", ""),
            source_type="fact_check",
            raw_claim_rating=review.get("textualRating", None),
            metadata={"claim_reviewed": item.get("text", "")},
        )
        sources.append(source)

    return sources