def test_create_doctor(client):
    response = client.post(
        "/doctors",
        json={
            "full_name": "Dr Omkaar",
            "specialization": "Neurology",
        },
    )

    assert response.status_code == 201
    data = response.json()
    assert data["full_name"] == "Dr Omkaar"
    assert data["id"] > 0


def test_get_doctors_empty(client):
    response = client.get("/doctors")
    assert response.status_code == 200
    assert response.json() == []


def test_get_doctors(client):
    client.post(
        "/doctors",
        json={
            "full_name": "Dr A",
            "specialization": "General",
        },
    )

    response = client.get("/doctors")
    assert response.status_code == 200
    assert len(response.json()) == 1


# def test_create_doctor_missing_specialization(client):
#     response = client.post(
#         "/doctors",
#         json={
#             "full_name": "Dr Missing",
#         },
#     )

#     assert response.status_code == 422


def test_create_inactive_doctor(client):
    response = client.post(
        "/doctors",
        json={
            "full_name": "Dr Missing",
            "specialization": "General",
            "is_active": False,
        },
    )

    assert response.status_code == 201
    assert response.json()["is_active"] is False
