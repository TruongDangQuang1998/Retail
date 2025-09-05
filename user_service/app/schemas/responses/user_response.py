from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID

class UserResponse(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    role: str
    status: str

    class Config:
        orm_mode = True