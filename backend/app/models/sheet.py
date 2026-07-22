
from sqlalchemy import ForeignKey
from sqlalchemy import Column
import uuid
from pydantic import Field
from sqlmodel import SQLModel
from typing import Optional, Dict
from sqlalchemy.dialects.postgresql import JSONB
from datetime import datetime, timezone

class Sheet(SQLModel, table=True):
    id: uuid.UUID = Field(default=uuid.uuid4, primary_key=True, index=True)
    workbook_id: uuid.UUID = Field(sa_column=Column(ForeignKey("workbooks.id", ondelete="CASCADE")))
    name: str = Field(unique=True, max_length=100, nullable=False)
    index: int = Field(default=0, nullable=False)
    data: Optional[Dict] = Field(default=None, sa_column=Column(JSONB))
    last_synced_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    version: int = Field(default=0)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
