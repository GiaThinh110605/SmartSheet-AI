
from sqlalchemy.dialects.postgresql import JSONB
import uuid
from typing import Optional, Dict
from sqlmodel import Field, SQLModel
from datetime import timezone, datetime
from sqlalchemy import Column

class User(SQLModel, table=True):
    __tablename__ = "users"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True, nullable=False)
    email: str = Field(unique=True, index=True, max_length=255, nullable=False)
    name: Optional[str] = Field(default=None, max_length=100)
    avatar_url: Optional[str] = Field(default=None)
    hashed_password: str = Field(nullable=False)

    settings: Optional[Dict] = Field(default=None, sa_column=Column(JSONB))
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))