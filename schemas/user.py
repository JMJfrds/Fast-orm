from datetime import datetime

from pydantic import BaseModel, EmailStr


class BaseUser(BaseModel):
    name: str
    username: str
    email: EmailStr
    created_at: datetime