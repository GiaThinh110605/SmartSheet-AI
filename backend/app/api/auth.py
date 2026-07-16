
from app.core.dependency import get_current_user
from app.core.security import verify_password
from app.schemas.auth import UserLogin
from app.schemas.auth import Token
from app.db.session import SessionDep
from app.schemas.auth import UserRegister
from app.schemas.auth import UserOut
from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.db.session import get_db
from sqlmodel import select
from app.core.security import get_password_hash, create_access_token, create_refresh_token
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

@router.post("/login", response_model=Token)
def login(user_in: UserLogin, db: SessionDep):
    statement = select(User).where(User.email == user_in.email)
    user = db.exec(statement).first()
    if not user or not verify_password(user_in.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    return {
        "access_token": create_access_token({"sub": str(user.id)}),
        "token_type": "bearer",
        "refresh_token": create_refresh_token({"sub": str(user.id)})
    }

@router.post("/token", response_model=Token)
def token(db: SessionDep, form_data: OAuth2PasswordRequestForm = Depends()):
    """OAuth2 compatible token endpoint (accepts form data for Swagger UI)"""
    statement = select(User).where(User.email == form_data.username)
    user = db.exec(statement).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    return {
        "access_token": create_access_token({"sub": str(user.id)}),
        "token_type": "bearer",
        "refresh_token": create_refresh_token({"sub": str(user.id)})
    }

@router.get("/me", response_model=UserOut)
def me(user: User = Depends(get_current_user)):
    return user