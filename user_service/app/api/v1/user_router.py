from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.requests.user_request import UserCreate, UserLogin
from app.schemas.responses.user_response import UserResponse
from app.services.user_service import UserService
from app.db.database import get_db

router = APIRouter(prefix="/api/v1/users", tags=["Users"])  

@router.post("/register")#, response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        new_user = UserService.register_user(db, user.name, user.email, user.password)
        return new_user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.post("/login")#, response_model=UserResponse)
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    try:
        logged_in_user = UserService.login_user(db, user.email, user.password)
        return logged_in_user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/{user_id}")
def get_user(user_id: str, db: Session = Depends(get_db)):
    user = UserService.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user