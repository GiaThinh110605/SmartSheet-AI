
from app.db.session import SessionDep
from app.schemas.auth import UserRegister
from app.schemas.auth import UserOut
from fastapi import APIRouter, status, Depends, HTTPException
from app.db.session import get_db
from sqlmodel import select
from app.core.security import get_password_hash
from app.models.user import User

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register(user_in: UserRegister, db: SessionDep):
    statement = select(User).where(User.email == user_in.email)
    existing_user = db.exec(statement).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_pwd = get_password_hash(user_in.password)
    db_user = User(
        email=user_in.email,
        hashed_password=hashed_pwd,
        name=user_in.name
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user