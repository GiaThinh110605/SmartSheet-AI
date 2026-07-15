from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr
from uuid import UUID

class UserBase(BaseModel):
    email: EmailStr
    password: str

class UserRegister(UserBase):
    name: Optional[str] = None

class UserLogin(UserBase):
    pass

class UserOut(BaseModel):
    id: UUID
    email: EmailStr
    name: Optional[str]
    avatar_url: Optional[str]
    settings: Optional[str]
    created_at: datetime
    updated_at: datetime

    # vì pydantic mặc định chỉ đọc dữ liệu ở dạng dict
    # còn SQL trả về dưới dạng ORM object
    # sử dụng config để có thể đọc được dữ liệu từ ORM object
    class Config:
        from_attributes = True

class TokenBase(BaseModel):
    refresh_token: str

class Token(TokenBase):
    access_token: str
    token_type: str = "bearer"

class TokenRefreshRequest(TokenBase):
    pass
