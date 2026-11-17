from datetime import date, datetime

from sqlalchemy import (
    CheckConstraint,
    Date,
    DateTime,
    String,
    Text,
    func
)
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Application(Base):

    __tablename__ = "applications"

    __table_args__ = (
        CheckConstraint(
            "status IN ('Interested', 'Applied', 'Assessment', "
            "'Interview', 'Offered', 'Rejected', 'Withdrawn')",
            name="ck_applications_status"
        ),
    )

    # Primary key
    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    # Basic application information
    company_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    job_title: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    job_type: Mapped[str] = mapped_column(
        String(30),
        nullable=False
    )

    location: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True
    )

    work_mode: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True
    )

    job_url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )

    source: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    # Application status
    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="Interested",
        server_default="Interested"
    )

    # Important dates
    date_found: Mapped[date] = mapped_column(
        Date,
        nullable=False,
        default=date.today,
        server_default=func.current_date()
    )

    date_applied: Mapped[date | None] = mapped_column(
        Date,
        nullable=True
    )

    deadline: Mapped[date | None] = mapped_column(
        Date,
        nullable=True
    )

    # Additional information
    notes: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    # Timestamps
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now()
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now()
    )