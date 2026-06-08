from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_session
from app.models.schemas import (
    ClaimRequest,
    VerificationSubmitResponse,
    VerificationStatusResponse,
)
from app.services import verification_service

router = APIRouter()

# Shared 503 body for when Postgres is unreachable. The DB is a core dependency
# of this layer, not an optional cache, so we fail fast rather than pretend.
_DB_UNAVAILABLE = "Verification store is unavailable. Please retry shortly."


@router.post(
    "/verify",
    response_model=VerificationSubmitResponse,
    status_code=status.HTTP_202_ACCEPTED,
)
async def submit_verification(
    request: ClaimRequest,
    session: AsyncSession = Depends(get_session),
) -> VerificationSubmitResponse:
    """Accept a claim, start verification in the background, return the job id.

    Returns 202 immediately; the client polls GET /verify/{id} for the result.
    submit_job commits the pending row BEFORE scheduling the background task, so
    if the DB is down the commit raises here and no orphan task is ever started.
    """
    try:
        # submit_job takes the claim STRING, not the ClaimRequest object.
        job_id = await verification_service.submit_job(request.claim, session)
    except SQLAlchemyError:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=_DB_UNAVAILABLE,
        )
    return VerificationSubmitResponse(id=job_id, status="pending")


@router.get("/verify/{verification_id}", response_model=VerificationStatusResponse)
async def get_verification(
    verification_id: UUID,
    session: AsyncSession = Depends(get_session),
) -> VerificationStatusResponse:
    """Poll a verification job by id.

    200 with the job for ANY existing job (status pending/done/failed); a failed
    job is reported in the body, not via an error code. 404 only when the id
    matches no job. The HTTP code answers "did the lookup work"; the status
    field answers "what happened to the job".
    """
    try:
        verification = await verification_service.get_job(verification_id, session)
    except SQLAlchemyError:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=_DB_UNAVAILABLE,
        )
    if verification is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No verification found for that id.",
        )
    # ORM row -> HTTP response object (works because from_attributes=True).
    return VerificationStatusResponse.model_validate(verification)