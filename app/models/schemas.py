from pydantic import BaseModel, ConfigDict, Field, field_validator
#import basic class
#automatic type validation without separate error checking
#also allow automatic type conversion
from typing import Optional #allow field to be optional (not mandatory)
from datetime import datetime # used by the job response timestamps below
from uuid import UUID #the job id type, matches the UUID primary key on the Verification row

class ClaimRequest(BaseModel):
    claim: str = Field(..., min_length=3, max_length=1000) #required, reject blank/absurd input

    @field_validator("claim", mode="before")
    @classmethod
    def _strip_claim(cls, v):
        # trim whitespace before the length checks run, so "   " fails min_length
        return v.strip() if isinstance(v, str) else v

class SourceResult(BaseModel):
    url: str
    title: str
    stance: str
    stance_confidence: float #nli confidence
    credibility_tier: str #vefified, estimated, unverified
    credibility_score: float
    bias_rating: str | None = None #bias, only tier one has it
    factual_reporting: str | None = None
    method: str | None = None         # "sentence_nli" | "fact_check" (None only for legacy cached results)
    sentence_count: int | None = None # NLI: sentences read; None for fact-check
    evidence: str | None = None       # NLI: the single sentence that drove the stance
    snippet: str | None = None        # the analyzed text chunk (context for evidence)
    rating: str | None = None         # fact-check rating; None for NLI sources

class ClaimResponse(BaseModel):
    claim: str
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


# ---------------------------------------------------------------------------
# Async job envelope models (the backend layer).
# These wrap the pipeline output above; they do NOT replace it. ClaimResponse
# is the *result* of a finished job, nested inside the poll response below.
# ---------------------------------------------------------------------------

class VerificationSubmitResponse(BaseModel):
    """Returned by POST /verify with HTTP 202.

    The minimal handle the client needs to start polling. status is always
    "pending" at submit time; it is here so the client can read it uniformly
    without special-casing the submit reply.
    """
    id: UUID
    status: str  # "pending" at submit


class VerificationStatusResponse(BaseModel):
    """Returned by GET /verify/{id} with HTTP 200 for ANY existing job.

    The status field drives the client:
      "pending" -> keep polling
      "done"    -> read result
      "failed"  -> read error
    A failed job is reported here in the body, not via an HTTP error code; 404
    is reserved for an unknown id (handled in the route, not here).

    from_attributes=True lets the route build this straight off the ORM row
    (model_validate(verification)) since the field names match the Verification
    columns one-to-one.
    """
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    status: str
    # Populated only when status == "done". Stored on the row as the JSON dump
    # of a ClaimResponse, so it re-validates back into one cleanly.
    result: Optional[ClaimResponse] = None
    # Populated only when status == "failed".
    error: Optional[str] = None
    created_at: datetime
    completed_at: Optional[datetime] = None
    # Populated by the route only while status == "pending": how many pending
    # jobs are ahead of this one (0 = at the front). Null otherwise. Not an ORM
    # column, so it is set explicitly by the route, not via model_validate.
    queue_position: Optional[int] = None
    #blank command added to check push pipeline of name edit