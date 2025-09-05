from sqlalchemy import Column, String, Enum, Boolean, Date, ForeignKey, Index
from sqlalchemy.orm import relationship
from .base_model import BaseModel, Base

class Address(BaseModel):
    __tablename__ = "addresses"

    user_id = Column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    receiver_name = Column(String(100), nullable=False)
    phone_number = Column(String(15), nullable=False)
    address_line = Column(String(255), nullable=False)
    city = Column(String(100), nullable=False)
    district = Column(String(100), nullable=False)
    ward = Column(String(100), nullable=True)
    is_default = Column(Boolean, default=False)

    user = relationship("User", back_populates="addresses")