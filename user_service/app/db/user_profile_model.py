from sqlalchemy import Column, String, Enum, Boolean, Date, ForeignKey, Index
from sqlalchemy.orm import relationship
from .base_model import BaseModel, Base
import uuid
from sqlalchemy.dialects.postgresql import UUID

class UserProfile(BaseModel):
    __tablename__ = "user_profiles"

    user_id = Column(UUID(as_uuid=True),nullable=False, unique=True)
    full_name = Column(String(100), nullable=True)
    dob = Column(Date, nullable=True)
    gender = Column(Enum("male", "female", "other", name="gender_enum"), nullable=True)
    default_address = Column(String(255), nullable=True)
