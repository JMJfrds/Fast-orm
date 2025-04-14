from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_user():
    user_data = {
        "name": "Test User",
        "email": "test@example.com",
        "username": "testuser",
        "created_at": "2025-04-13T12:00:00"
    }
    response = client.post("/user/", json=user_data)
    assert response.status_code == 200
    res_data = response.json()
    assert "data" in res_data
    assert res_data["data"]["username"] == "testuser"


def test_read_users():
    response = client.get("/user/")
    assert response.status_code == 200
    res_data = response.json()
    assert "data" in res_data
    assert isinstance(res_data["data"], list)
    assert len(res_data["data"]) > 0
    global user_id  # saqlab qolamiz
    user_id = res_data["data"][0]["id"]


def test_update_user():
    updated_data = {
        "name": "Updated User",
        "email": "updated@example.com",
        "username": "updateduser",
        "created_at": "2025-04-13T12:00:00"
    }
    response = client.put(f"/user/{user_id}/", json=updated_data)
    assert response.status_code == 200
    res_data = response.json()
    assert "data" in res_data
    assert res_data["data"]["username"] == "updateduser"


def test_delete_user():
    response = client.delete(f"/user/{user_id}/")
    assert response.status_code == 200
    res_data = response.json()
    assert "data" in res_data
    assert res_data["data"]["id"] == user_id
