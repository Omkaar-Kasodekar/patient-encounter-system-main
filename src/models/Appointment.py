from datetime import datetime
from typing import TYPE_CHECKING
from sqlalchemy import Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base

if TYPE_CHECKING:
    from src.models.Patient import Patient
    from src.models.Doctor import Doctor


class Appointment(Base):
    __tablename__ = "omkar_appointments"

    id: Mapped[int] = mapped_column(primary_key=True)

    patient_id: Mapped[int] = mapped_column(
        ForeignKey("omkaar_patients.id"), nullable=False
    )
    doctor_id: Mapped[int] = mapped_column(
        ForeignKey("omkaar_doctors.id"), nullable=False
    )

    start_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, index=True
    )
    duration_minutes: Mapped[int] = mapped_column(Integer, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.utcnow, nullable=False
    )

    patient: Mapped["Patient"] = relationship(
        "Patient",
        back_populates="appointments",
    )
    doctor: Mapped["Doctor"] = relationship(
        "Doctor",
        back_populates="appointments",
    )
