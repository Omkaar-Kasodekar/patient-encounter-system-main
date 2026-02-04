from datetime import datetime, timezone
from pydantic import BaseModel, EmailStr, Field, field_validator as validator
from pydantic import ConfigDict


class PatientCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str


class PatientRead(PatientCreate):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class DoctorCreate(BaseModel):
    full_name: str
    specialization: str
    is_active: bool = True


class DoctorRead(DoctorCreate):
    id: int
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class AppointmentCreate(BaseModel):
    patient_id: int
    doctor_id: int
    start_time: datetime
    duration_minutes: int = Field(ge=15, le=180)

    @validator("start_time")
    def ensure_timezone(cls, value):
        if value.tzinfo is None:
            return value.replace(tzinfo=timezone.utc)
        return value


class AppointmentRead(AppointmentCreate):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
