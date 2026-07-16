from datetime import timedelta
from datetime import datetime
import bcrypt
import jwt
from app.core.config import settings

def get_password_hash(password: str) -> str:
    password_bytes = password.encode("utf-8")
    
    salt = bcrypt.gensalt()
    hashed_pwd = bcrypt.hashpw(password_bytes, salt)
    return hashed_pwd.decode("utf-8")

def verify_password(password, hashpassword):
    return bcrypt.checkpw(
        password.encode("utf-8"),
        hashpassword.encode("utf-8")
    )

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire, "type": "access"})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def create_refresh_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=7)
    to_encode.update({"exp": expire, "type": "refresh"})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)