from pydantic import BaseModel, Field, field_validator, model_validator
#import basic class
#automatic type validation without separate error checking
#also allow automatic type conversion
from typing import Optional #allow field to be optional (not mandatory)
from datetime import date, timedelta # allow date field to come up

class ClaimRequest(BaseModel):
    claim: str = Field(..., min_length=3, max_length=1000) #required, reject blank/absurd input
    # default_factory so "today" is recomputed per request, not frozen at import time
    date_range_start: Optional[date] = Field(default_factory=lambda: date.today() - timedelta(days=5*365)) #defualt to 5 years if not provided
    date_range_end: Optional[date] = Field(default_factory=lambda: date.today()) #default to today if not provided

    @field_validator("claim", mode="before")
    @classmethod
    def _strip_claim(cls, v):
        # trim whitespace before the length checks run, so "   " fails min_length
        return v.strip() if isinstance(v, str) else v

    @model_validator(mode="after")
    def _check_date_order(self):
        if self.date_range_start and self.date_range_end and self.date_range_start > self.date_range_end:
            raise ValueError("date_range_start must be on or before date_range_end")
        return self

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
    claim_domain: str #topic bucket (science, politics, health, ...) used for source routing
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