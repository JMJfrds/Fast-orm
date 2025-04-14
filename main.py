from fastapi import FastAPI
from pydantic import BaseModel

from db import init_db
from config import get_settings
from schemas.user import BaseUser
from schemas.base import BaseResponse
from models.user import User


settings = get_settings()


app = FastAPI(
    title = settings.app_name,
    version = settings.app_version,
    description = "FastAPI CRUD Tortoise-orm with aerich",
    debug = settings.app_debug
)

@app.on_event("startup")
async def startup():
    await init_db()
    print("Database initialized")


@app.post("/user/", response_model = BaseResponse)
async def create_user(user: BaseUser):
    user_data = await User.create(
        name = user.name,
        email = user.email,
        username = user.username,
        created_at = user.created_at,
    )

    data = {
        "name": user_data.name,
        "username": user_data.username,
        "email": user_data.email,
        "created_at": user_data.created_at,
    }
    return BaseResponse(data = data)


@app.get("/user/", response_model = BaseResponse)
async def read_users():
    users = await User.all()
    data = [
        {   "id":user.id,
            "name": user.name,
            "email": user.email,
            "username": user.username
        }
        for user in users
    ]
    return BaseResponse(data=data)


@app.put("/user/{user_id}/", response_model = BaseResponse)
async def update_user(user_id: int, user: BaseUser):
    user_data = await User.get_or_none(id = user_id)

    if not user_data:
        return BaseResponse(data = {"error": "user not found"})

    user_data.name = user.name
    user_data.username = user.username
    user_data.email = user.email

    await user_data.save()

    new_data = {
        "name": user_data.name,
        "email": user_data.email,
        "username": user_data.username,
    }
    return BaseResponse(data = new_data)


@app.delete("/user/{user_id}/", response_model = BaseResponse)
async def delete_user(user_id: int):
    user_data = await User.get_or_none(id = user_id)

    if not user_data:
        return BaseResponse(data = {"error": "user not found"})

    await user_data.delete()
    return BaseResponse(data={"id": user_id})
