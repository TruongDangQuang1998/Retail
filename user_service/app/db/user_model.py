from sqlalchemy import Column, String, Enum, Boolean, Date, ForeignKey, Index
from sqlalchemy.orm import relationship
import enum
from .base_model import BaseModel, Base
from app.db.user_profile_model import UserProfile

class UserRole(enum.Enum):
    ADMIN = "admin"
    USER = "user"
    STAFF = "staff"

class UserStatus(enum.Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"

class User(BaseModel):
    __tablename__ = "users"

    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    phone_number = Column(String(15), unique=True, nullable=True, index=True)
    password_hash = Column(String, nullable=False)
    role = Column(Enum(UserRole), default=UserRole.USER, nullable=False)
    status = Column(Enum(UserStatus), default=UserStatus.ACTIVE, nullable=False)
    # profile = relationship("UserProfile", back_populates="user", uselist=False, cascade="all, delete-orphan")
    # addresses = relationship("Address", back_populates="user", cascade="all, delete-orphan")


    # # Relationships
    # created_items = relationship("Item", back_populates="creator", foreign_keys='Item.created_by')
    # updated_items = relationship("Item", back_populates="updater", foreign_keys='Item.updated_by')

    # __table_args__ = (
    #     Index('ix_users_email_username', 'email', 'username'),
    # )