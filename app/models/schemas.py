from pydantic import BaseModel
#import basic class
#automatic type validation without separate error checking
#also allow automatic type conversion
from typing import Optional #allow field to be optional (not mandatory)
from datetime import date, timedelta # allow date field to come up

class ClaimRequest(BaseModel):
    claim: str #required
    date_range_start: Optional[date] = date.today() - timedelta(days=5*365) #defualt to 5 years if not provided
    date_range_end: Optional[date] = date.today() #default to today if not provided

class SourceResult(BaseModel):
    url: str
    title: str
    stance: str
    stance_confidence: float #nli confidence
    credibility_tier: str #vefified, estimated, unverified
    credibility_score: float
    bias_rating: str | None = None #bias, only tier one has it
    factual_reporting: str | None = None
    support_summary: str

class ClaimResponse(BaseModel):
    claim: str
    claim_type: str #opinion vs factual
    claim_type_confidence: float #how confident are you on the fact that it is opinon or factual
    verdict: str
    confidence_in_verdict: float
    sources: list[SourceResult]

class Source(BaseModel):
    url: str
    title: str
    snippet: str
    source_type: str      # "fact_check", "news", "encyclopedia", "academic", "web"
    credibility: Optional[float] = None  # 0.0 to 1.0, filled in later
    raw_claim_rating: Optional[str] = None  # only for fact-checks, e.g. "False", "Mostly True"
    metadata: dict | None = None #used to count how many other sources each source used, etc..

