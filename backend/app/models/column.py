from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
import uuid
from typing import Optional, Dict
from sqlmodel import SQLModel, Field
from datetime import datetime, timezone

class SheetColumn(SQLModel, table=True):
    __tablename__ = "columns"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, nullable=False, index=True)
    sheet_id: uuid.UUID = Field(sa_column=Column(ForeignKey("sheets.id", ondelete="CASCADE")))
    col_index: int = Field(nullable=False)
    name: str = Field(max_length=150, nullable=False)
    data_type: str = Field(max_length=50, nullable=False)
    format_options: Optional[Dict] = Field(default=None, sa_column=Column(JSONB))
    is_required: bool = Field(default=False)
    default_value: Optional[str] = Field(default=None)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
