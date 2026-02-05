def test_create_patient(client):
    response = client.post(
        "/patients",
        json={
            "first_name": "Omkaar",
            "last_name": "Kasodekar",
            "email": "ok@test.com",
            "phone_number": "9999999999",
        },
    )

    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "ok@test.com"
    assert data["id"] > 0


def test_get_patients_empty(client):
    response = client.get("/patients")
    assert response.status_code == 200
    assert response.json() == []


def test_get_patients(client):
    client.post(
        "/patients",
        json={
            "first_name": "A",
            "last_name": "B",
            "email": "a@test.com",
            "phone_number": "8888888888",
        },
    )

    response = client.get("/patients")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_create_patient_duplicate_email(client):
    payload = {
        "first_name": "A",
        "last_name": "B",
        "email": "dup@test.com",
        "phone_number": "7777777777",
    }

    client.post("/patients", json=payload)
    response = client.post("/patients", json=payload)

    assert response.status_code == 400


# def test_create_patient_missing_field(client):
#     response = client.post(
#         "/patients",
#         json={
#             "first_name": "A",
#             "email": "x@test.com",
#             "phone_number": "9999999999",
#         },
#     )

#     assert response.status_code == 422


# def test_create_patient_invalid_email(client):
#     response = client.post(
#         "/patients",
#         json={
#             "first_name": "A",
#             "last_name": "B",
#             "email": "invalid",
#             "phone_number": "9999999999",
#         },
#     )

#     assert response.status_code == 422
