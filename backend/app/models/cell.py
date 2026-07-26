from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
import uuid
from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime, timezone

class Cell(SQLModel, table=True):
    __tablename__ = "cells"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, nullable=False, index=True)
    sheet_id: uuid.UUID = Field(sa_column=Column(ForeignKey("sheets.id", ondelete="CASCADE")))
    row_index: int = Field(nullable=False)
    col_index: int = Field(nullable=False)
    value: Optional[str] = Field(default=None)
    computed_value: Optional[str] = Field(default=None)
    status: Optional[str] = Field(default=None, max_length=30)
    version: int = Field(default=0)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
