from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List
from sqlalchemy import select

from src.database import engine, get_db, Base
from src.models.Patient import Patient
from src.models.Doctor import Doctor
from src.models.Appointment import Appointment
from src.schemas import (
    PatientCreate,
    DoctorCreate,
    AppointmentCreate,
    PatientRead,
    DoctorRead,
    AppointmentRead,
)
from src.services.services import (
    create_patient,
    create_doctor,
    schedule_appointment,
)

app = FastAPI(title="Medical Encounter Management System")


Base.metadata.create_all(bind=engine)


@app.post("/patients", response_model=PatientRead, status_code=201)
def create_patient_api(
    patient: PatientCreate,
    db: Session = Depends(get_db),
):
    obj = Patient(**patient.dict())
    return create_patient(db, obj)


@app.post("/doctors", response_model=DoctorRead, status_code=201)
def create_doctor_api(
    doctor: DoctorCreate,
    db: Session = Depends(get_db),
):
    obj = Doctor(**doctor.dict())
    return create_doctor(db, obj)


@app.post("/appointments", response_model=AppointmentRead, status_code=201)
def create_appointment_api(
    appointment: AppointmentCreate,
    db: Session = Depends(get_db),
):
    obj = Appointment(**appointment.dict())
    return schedule_appointment(db, obj)


@app.get("/doctors", response_model=List[DoctorRead])
def get_doctors(db: Session = Depends(get_db)):
    return db.execute(select(Doctor)).scalars().all()


@app.get("/patients", response_model=List[PatientRead])
def get_patients(db: Session = Depends(get_db)):
    return db.execute(select(Patient)).scalars().all()


@app.get("/appointments", response_model=List[AppointmentRead])
def get_appointments(db: Session = Depends(get_db)):
    return db.execute(select(Appointment)).scalars().all()
