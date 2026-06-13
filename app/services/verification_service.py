import asyncio
import logging
import os
import uuid
from datetime import datetime, timezone

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import AsyncSessionLocal
from app.db.models import Verification
from app.models.schemas import ClaimRequest
from app.services.claim_service import analyze_claim

logger = logging.getLogger(__name__)

# A job that has STARTED running but not finished within this many seconds is
# treated as dead (e.g. the server restarted mid-run) and flipped to failed the
# next time it is polled. Measured from started_at, NOT created_at: a job still
# waiting in the admission queue has not started and is never stale. Comfortably
# above the normal ~10s pipeline time. Tunable.
STALE_AFTER_SECONDS = 300

# --- Admission control (backpressure) -------------------------------------
# Two independent limits:
#   MAX_CONCURRENT_PIPELINES: how many jobs may RUN the pipeline at once. The
#     rest are accepted but wait at the semaphore (cheap, no CPU/GPU used while
#     waiting). Sized to where measured latency stays acceptable on this box.
#   MAX_QUEUE_DEPTH: how many jobs may be in-flight (pending OR running) before
#     submit refuses with a 429. This is the hard ceiling that bounds the worst-
#     case wait: the semaphore alone would just let an unbounded line form, this
#     caps the line. Sized so depth/concurrency * per-claim-time stays tolerable.
# Both are env knobs so they can be tuned per hardware without a code change.
MAX_CONCURRENT_PIPELINES = int(os.getenv("MAX_CONCURRENT_PIPELINES", "3"))
MAX_QUEUE_DEPTH = int(os.getenv("MAX_QUEUE_DEPTH", "12"))

# Rough per-claim wall time (seconds), used only to estimate a Retry-After / ETA
# hint for clients. Not load-bearing; approximate is fine.
EST_SECONDS_PER_CLAIM = int(os.getenv("EST_SECONDS_PER_CLAIM", "10"))

# Limits concurrent pipeline execution. Created lazily on the running loop (a
# module-level asyncio.Semaphore would bind to whatever loop imported it, which
# is fragile under tests); _get_sem returns the one bound to the current loop.
_pipeline_sem: asyncio.Semaphore | None = None


def _get_sem() -> asyncio.Semaphore:
    global _pipeline_sem
    if _pipeline_sem is None:
        _pipeline_sem = asyncio.Semaphore(MAX_CONCURRENT_PIPELINES)
    return _pipeline_sem


# Holds references to in-flight background tasks so the event loop does not
# garbage-collect them mid-run. Each task removes itself on completion.
_background_tasks: set[asyncio.Task] = set()


class QueueFullError(Exception):
    """Raised by submit_job when in-flight jobs are at MAX_QUEUE_DEPTH.

    Carries a suggested retry delay (seconds) for the Retry-After header.
    """

    def __init__(self, depth: int, retry_after: int):
        self.depth = depth
        self.retry_after = retry_after
        super().__init__(f"queue full: {depth} jobs in flight")


# In-flight count: jobs accepted but not yet finished. A plain int, NOT a DB
# count, on purpose. A "count pending rows in the DB then decide" check races
# under burst: many concurrent submissions all run their COUNT before any of
# them commits its insert, so they all see a low number and all pass the gate.
# Because every submission runs on the single event loop, incrementing this
# counter in submit_job and decrementing it when the job finishes is atomic
# relative to other submissions (no two coroutines mutate it simultaneously),
# so it is the accurate, race-free in-flight number.
_inflight: int = 0


#what adds the task to the row in the table
async def submit_job(claim: str, session: AsyncSession) -> uuid.UUID:
    """Insert a pending row, start the pipeline in the background, return the id.

    Admission control: if too many jobs are already in flight, refuse with
    QueueFullError (the route turns it into 429) BEFORE inserting a row, so a
    rejected request leaves no trace and consumes no work. The check and the
    increment happen with no await between them, so the gate cannot be raced.
    """
    global _inflight
    if _inflight >= MAX_QUEUE_DEPTH:
        retry_after = max(1, (_inflight // MAX_CONCURRENT_PIPELINES) * EST_SECONDS_PER_CLAIM)
        raise QueueFullError(depth=_inflight, retry_after=retry_after)

    # Reserve the slot synchronously (before the first await) so concurrent
    # submissions on the same loop see the updated count immediately.
    _inflight += 1
    try:
        verification = Verification(claim=claim)
        session.add(verification)
        await session.commit()
        job_id = verification.id
    except Exception:
        # Insert failed: release the reserved slot so a DB error does not leak
        # in-flight capacity permanently.
        _inflight -= 1
        raise

    task = asyncio.create_task(run_job(job_id))
    _background_tasks.add(task)
    task.add_done_callback(_background_tasks.discard)

    return job_id


#actually run the nli
async def run_job(verification_id: uuid.UUID) -> None:
    """Background worker: run the pipeline and record the outcome on the row.

    Runs detached from any request, so it opens its own session. Acquires the
    concurrency semaphore BEFORE running the pipeline: if MAX_CONCURRENT_PIPELINES
    are already running, this awaits here (the row stays "pending", no CPU/GPU
    used while waiting) until a slot frees. started_at is stamped at the moment
    work actually begins, which is what staleness is measured from.
    """
    global _inflight
    try:
        async with _get_sem():
            async with AsyncSessionLocal() as session:
                verification = await session.get(Verification, verification_id)
                if verification is None:
                    logger.error("run_job: verification %s vanished before run", verification_id)
                    return

                # Mark the start of actual work (used by the stale check).
                verification.started_at = datetime.now(timezone.utc)
                await session.commit()

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
    finally:
        # Release the in-flight slot no matter how the job ended (done, failed,
        # vanished, or crashed). Pairs with the increment in submit_job.
        _inflight -= 1


#this is what does polling
async def get_job(verification_id: uuid.UUID, session: AsyncSession) -> Verification | None:
    """Fetch a job by id. Lazily fails jobs that have been running too long."""
    verification = await session.get(Verification, verification_id)
    if verification is None:
        return None

    if verification.status == "pending" and _is_stale(verification):
        verification.status = "failed"
        verification.error = "job did not complete (server likely restarted mid-run)"
        verification.completed_at = datetime.now(timezone.utc)
        await session.commit()

    return verification


async def queue_position(verification_id: uuid.UUID, session: AsyncSession) -> int | None:
    """For a still-pending job, how many pending jobs were created before it.

    0 means it is at the front (running or next up). None if the job is not
    pending (already done/failed) or not found.
    """
    verification = await session.get(Verification, verification_id)
    if verification is None or verification.status != "pending":
        return None
    result = await session.execute(
        select(func.count()).select_from(Verification).where(
            Verification.status == "pending",
            Verification.created_at < verification.created_at,
        )
    )
    return int(result.scalar_one())


#time out check
def _is_stale(verification: Verification) -> bool:
    # A job that has not started yet (still queued) is never stale: it is
    # legitimately waiting for a concurrency slot, not hung.
    if verification.started_at is None:
        return False
    age = datetime.now(timezone.utc) - verification.started_at
    return age.total_seconds() > STALE_AFTER_SECONDS