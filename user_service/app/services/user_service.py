from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.db.user_model import User
import bcrypt
from fastapi import HTTPException, status

class UserService:
    @staticmethod
    def register_user(db: Session, name:str, email:str, password:str)-> User:
        existing_user = UserRepository.get_user_by_email(db,email)
        if existing_user:
            raise ValueError("Email already registered")
        return UserRepository.create_user(db, name,email,password)
    
    @staticmethod
    def login_user(db: Session, email:str, password:str)-> User:
        user = UserRepository.get_user_by_email(db,email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )
        # if not user or not bcrypt.checkpw(password.encode("utf-8"), user.password_hash.endcode("utf-8")):
        #     raise ValueError("Invalid email or password")
        if not bcrypt.checkpw(password.encode("utf-8"), user.password_hash.encode("utf-8")):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )
        return user
    
    @staticmethod
    def get_user(db: Session, user_id: str)-> User:
        return UserRepository.get_user_by_id(db, user_id)