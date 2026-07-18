
from sqlalchemy import ForeignKey
from time import timezone
from typing import Optional, Dict
import uuid
from sqlmodel import SQLModel
from fastapi import Field
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import Column

class Workbook(SQLModel, table=True):
    __tablename__ = "workbooks"

    id: uuid.UUID = Field(default=uuid.uuid4, primary_key=True, nullable=False, index=True)
    user_id: uuid.UUID = Field(sa_column=Column(ForeignKey("users.id", ondelete="CASCADE")), nullable=False)
    name: str = Field(unique=True, max_length=200, nullable=False)
    description: Optional[str] = Field(default=None)
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    metadata: Optional[Dict] = Field(default=None, sa_column=Column(JSONB))