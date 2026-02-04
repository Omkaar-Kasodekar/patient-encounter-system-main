# from datetime import datetime, timedelta, timezone


# # def create_patient_and_doctor(client):
# #     patient = client.post(
# #         "/patients",
# #         json={
# #             "first_name": "Jane",
# #             "last_name": "Doe",
# #             "email": "jane@test.com",
# #             "phone_number": "8888888888",
# #         },
# #     ).json()

# #     doctor = client.post(
# #         "/doctors",
# #         json={
# #             "full_name": "Dr Who",
# #             "specialization": "General",
# #         },
# #     ).json()

# #     return patient["id"], doctor["id"]


# def test_create_appointment(client):
#     patient_id, doctor_id = create_patient_and_doctor(client)

#     start_time = (datetime.now(timezone.utc) + timedelta(days=1)).isoformat()

#     response = client.post(
#         "/appointments",
#         json={
#             "patient_id": patient_id,
#             "doctor_id": doctor_id,
#             "start_time": start_time,
#             "duration_minutes": 30,
#         },
#     )

#     assert response.status_code == 201
#     assert response.json()["patient_id"] == patient_id


# def test_appointment_overlap(client):
#     patient_id, doctor_id = create_patient_and_doctor(client)

#     start_time = datetime.now(timezone.utc) + timedelta(days=1)

#     client.post(
#         "/appointments",
#         json={
#             "patient_id": patient_id,
#             "doctor_id": doctor_id,
#             "start_time": start_time.isoformat(),
#             "duration_minutes": 60,
#         },
#     )

#     response = client.post(
#         "/appointments",
#         json={
#             "patient_id": patient_id,
#             "doctor_id": doctor_id,
#             "start_time": (start_time + timedelta(minutes=30)).isoformat(),
#             "duration_minutes": 30,
#         },
#     )

#     assert response.status_code == 409
#     assert response.json()["detail"] == "Doctor has a overlap"


# def test_appointment_boundary_no_overlap(client):
#     patient_id, doctor_id = create_patient_and_doctor(client)

#     start_time = datetime.now(timezone.utc) + timedelta(days=1)

#     client.post(
#         "/appointments",
#         json={
#             "patient_id": patient_id,
#             "doctor_id": doctor_id,
#             "start_time": start_time.isoformat(),
#             "duration_minutes": 30,
#         },
#     )

#     response = client.post(
#         "/appointments",
#         json={
#             "patient_id": patient_id,
#             "doctor_id": doctor_id,
#             "start_time": (start_time + timedelta(minutes=30)).isoformat(),
#             "duration_minutes": 30,
#         },
#     )

#     assert response.status_code == 201


# def test_create_appointment_invalid_patient(client):
#     response = client.post(
#         "/appointments",
#         json={
#             "patient_id": 999,
#             "doctor_id": 1,
#             "start_time": datetime.now(timezone.utc).isoformat(),
#             "duration_minutes": 30,
#         },
#     )

#     assert response.status_code == 404


# def test_create_appointment_invalid_doctor(client):
#     response = client.post(
#         "/appointments",
#         json={
#             "patient_id": 1,
#             "doctor_id": 999,
#             "start_time": datetime.now(timezone.utc).isoformat(),
#             "duration_minutes": 30,
#         },
#     )

#     assert response.status_code == 404


# def test_create_appointment_in_past(client):
#     patient_id, doctor_id = create_patient_and_doctor(client)

#     response = client.post(
#         "/appointments",
#         json={
#             "patient_id": patient_id,
#             "doctor_id": doctor_id,
#             "start_time": (datetime.now(timezone.utc) - timedelta(days=1)).isoformat(),
#             "duration_minutes": 30,
#         },
#     )

#     assert response.status_code == 400


# def test_create_appointment_invalid_duration(client):
#     patient_id, doctor_id = create_patient_and_doctor(client)

#     response = client.post(
#         "/appointments",
#         json={
#             "patient_id": patient_id,
#             "doctor_id": doctor_id,
#             "start_time": datetime.now(timezone.utc).isoformat(),
#             "duration_minutes": 0,
#         },
#     )

#     assert response.status_code == 422


# def test_get_appointments(client):
#     response = client.get("/appointments")
#     assert response.status_code == 200
#     assert isinstance(response.json(), list)
