from app.models import ClaimRequest, SourceResult, ClaimResponse
import heapq
'''
    class ClaimRequest(BaseModel):
        claim: str #required
        date_range_start: Optional[date] = date.today() - timedelta(days=5*365) #defualt to 5 years if not provided
        date_range_end: Optional[date] = date.today() #default to today if not provided

    class SourceResult(BaseModel):
        url: str
        title: str
        stance: str
        reliability: float # gonna be percentage
        support_summary: str

    class ClaimResponse(BaseModel):
        verdict: str
        confidence_in_verdict: float #also percentage
        sources: list[SourceResult]
'''

def analyze_claim(request: ClaimRequest) -> ClaimResponse:
    raw_sources = search_sources(request.claim) #receive dictionary of all sources

    analyzed_sources = analyze_sources(request.claim, raw_sources) #receive Source Result objects

    verdict, confidence_in_verdict = compute_verdict(analyzed_sources) #receive the verdict and the confidence of overall verdict

    return ClaimResponse(verdict=verdict, confidence_in_verdict=confidence_in_verdict, sources=analyzed_sources)


def search_sources(claim: str) -> list[dict]:
    # TODO: implement real source searching
    return [
        {"url": "https://example.com", "title": "Example Source", "content": "Placeholder content"}
    ]


def analyze_sources(claim: str, raw_sources: list[dict]) -> list[SourceResult]:
    # TODO: implement NLI stance detection
    results = []

    for source in raw_sources:
        results.append(
            SourceResult(
                url=source["url"],
                title=source["title"],
                stance="opposing",
                reliability=0.85,
                support_summary="Placeholder analysis."
            )
        )
    return results


def compute_verdict(source_results_list: list[SourceResult]) -> tuple[str, float]:
    supportPercentage = 0
    supportList = []
    againstPercentage = 0
    againstList = []

    for sourceResult in source_results_list:
        #ok, i do think calculation should be somewhat more complex than this in the future
        #right now, it is still rewarding the source with more support, but idk maybe i should heavily penalize them?
        #let's do top 3? in case there are no 3 sources, than we can penalize them naturally
        #TODO: improve this logic...

        if sourceResult.stance == "opposing":
            heapq.heappush(againstList, (sourceResult.reliability, sourceResult))
        else:
            heapq.heappush(supportList, (sourceResult.reliability, sourceResult))

    #grab top 3 most reliable from each side
    for reliability, source in heapq.nlargest(3, supportList):
        supportPercentage += reliability

    for reliability, source in heapq.nlargest(3, againstList):
        againstPercentage += reliability

    finalVerdict = ""
    finalConfidence = 0.0

    if supportPercentage > againstPercentage:
        finalVerdict = "supporting"
    elif supportPercentage == againstPercentage:
        finalVerdict = "inconclusive"
    else:
        finalVerdict = "opposing"

    #calculating confidence: simple ratio for now, will improve with NLI integration
    #TODO: improve confidence calculation
    total = supportPercentage + againstPercentage
    if total > 0:
        finalConfidence = abs(supportPercentage - againstPercentage) / total
    else:
        finalConfidence = 0.0

    return (finalVerdict, finalConfidence)