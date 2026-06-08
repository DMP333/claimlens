import asyncio
import logging
import uuid
from datetime import datetime, timezone

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import AsyncSessionLocal
from app.db.models import Verification
from app.models.schemas import ClaimRequest
from app.services.claim_service import analyze_claim

logger = logging.getLogger(__name__)

# A pending job older than this is treated as dead (e.g. the server restarted
# mid-run) and flipped to failed the next time it is polled. Comfortably above
# the normal ~10s pipeline time. Tunable.
STALE_AFTER_SECONDS = 300

# Holds references to in-flight background tasks so the event loop does not
# garbage-collect them mid-run. Each task removes itself on completion.
_background_tasks: set[asyncio.Task] = set()


#what adds the task to the row in the table
async def submit_job(claim: str, session: AsyncSession) -> uuid.UUID:
    """Insert a pending row, start the pipeline in the background, return the id."""
    verification = Verification(claim=claim)
    session.add(verification)
    await session.commit()

    job_id = verification.id

    task = asyncio.create_task(run_job(job_id))
    _background_tasks.add(task)
    task.add_done_callback(_background_tasks.discard)

    return job_id

#actually run the nli
async def run_job(verification_id: uuid.UUID) -> None:
    """Background worker: run the pipeline and record the outcome on the row.

    Runs detached from any request, so it opens its own session.
    """
    async with AsyncSessionLocal() as session:
        verification = await session.get(Verification, verification_id)
        if verification is None:
            logger.error("run_job: verification %s vanished before run", verification_id)
            return

        try:
            result = await analyze_claim(ClaimRequest(claim=verification.claim))
            verification.status = "done"
            verification.result = result.model_dump(mode="json")
        except Exception as exc:  # noqa: BLE001 - every failure must be recorded
            logger.exception("run_job: pipeline failed for %s", verification_id)
            verification.status = "failed"
            verification.error = str(exc)

        verification.completed_at = datetime.now(timezone.utc)
        await session.commit()

#this is what does polling
async def get_job(verification_id: uuid.UUID, session: AsyncSession) -> Verification | None:
    """Fetch a job by id. Lazily fails jobs that have been pending too long."""
    verification = await session.get(Verification, verification_id)
    if verification is None:
        return None

    if verification.status == "pending" and _is_stale(verification):
        verification.status = "failed"
        verification.error = "job did not complete (server likely restarted mid-run)"
        verification.completed_at = datetime.now(timezone.utc)
        await session.commit()

    return verification

#time out check
def _is_stale(verification: Verification) -> bool:
    age = datetime.now(timezone.utc) - verification.created_at
    return age.total_seconds() > STALE_AFTER_SECONDS