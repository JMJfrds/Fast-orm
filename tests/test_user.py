import pytest
from httpx import AsyncClient
from main import app
from tortoise.contrib.test import initializer, finalizer


@pytest.fixture(scope="module", autouse=True)
def initialize_db():
    initializer(["models.user"])
    yield
    finalizer()


@pytest.mark.asyncio
async def test_crud_user():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # 1. Create user
        user_payload = {
            "name": "Jasmina",
            "email": "jasmina@example.com",
            "username": "jasmina",
            "created_at": "2025-04-13T12:00:00"
        }
        create_res = await ac.post("/user/", json=user_payload)
        assert create_res.status_code == 200
        assert create_res.json()["data"]["username"] == "jasmina"

        # 2. Read users
        read_res = await ac.get("/user/")
        assert read_res.status_code == 200
        assert len(read_res.json()["data"]) > 0
        user_id = read_res.json()["data"][0]["id"]

        # 3. Update user
        updated_data = {
            "name": "Jasmina Updated",
            "email": "jasmina_new@example.com",
            "username": "jasmina_new",
            "created_at": "2025-04-13T12:00:00"
        }
        update_res = await ac.put(f"/user/{user_id}/", json=updated_data)
        assert update_res.status_code == 200
        assert update_res.json()["data"]["username"] == "jasmina_new"

        # 4. Delete user
        delete_res = await ac.delete(f"/user/{user_id}/")
        assert delete_res.status_code == 200
        assert delete_res.json()["data"]["id"] == user_id
