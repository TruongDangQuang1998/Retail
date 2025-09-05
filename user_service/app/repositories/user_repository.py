from sqlalchemy.orm import Session
from app.db.user_model import User, UserRole, UserStatus
from uuid import uuid4
import bcrypt

class UserRepository:
    @staticmethod
    def create_user(db: Session, name: str, email: str, password: str)-> User:
        hashed_pw = bcrypt.hashpw(password.encode("utf-8"),bcrypt.gensalt()).decode("utf-8")
        new_user = User(
            id=uuid4(),
            username=name,
            email = email,
            password_hash = hashed_pw,
            role = UserRole.USER,
            status = UserStatus.ACTIVE
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    
    @staticmethod
    def get_user_by_email(db: Session, email:str) -> User:
        return db.query(User).filter(User.email == email).first()
    
    @staticmethod
    def get_user_by_id(db: Session, id: str) -> User:
        return db.query(User).filter(User.id == id).first()