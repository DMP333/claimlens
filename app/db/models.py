import uuid
from datetime import datetime, timezone

from sqlalchemy import String, Text, DateTime, Uuid
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base

#Verification is a one row of the table
#multiple verificatin row combines to create a table
#this class describes the shape of the Verification row

class Verification(Base):
    #we inherit base and build a table named verification
    #This file is nothing but the blue print, no function call
    __tablename__ = "verifications"

    # Non-guessable primary key so a result URL cannot be enumerated.
    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4,
    )

    # The claim text the user submitted.
    claim: Mapped[str] = mapped_column(Text, nullable=False)

    # Job lifecycle: "pending" -> "done" or "failed". Set only by our service.
    status: Mapped[str] = mapped_column(String(16), nullable=False, default="pending")

    # Full pipeline output, serialized. Null until the job finishes successfully.
    result: Mapped[dict | None] = mapped_column(JSONB, nullable=True)

    # Failure message. Null unless the pipeline raised.
    error: Mapped[str | None] = mapped_column(Text, nullable=True)

    # When the row was inserted. App-side clock so the value is known immediately.
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    # When the job actually BEGAN running the pipeline (acquired the concurrency
    # slot). Null while still queued. Staleness is measured from THIS, not from
    # created_at, so a job that legitimately waits in the admission queue is not
    # mistaken for a hung job.
    started_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    # When the job reached done or failed. Null while still pending.
    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )