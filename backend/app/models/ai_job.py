from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
import uuid
from typing import Optional, Dict
from sqlmodel import SQLModel, Field
from datetime import datetime, timezone

class AIJob(SQLModel, table=True):
    __tablename__ = "ai_jobs"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, nullable=False, index=True)
    sheet_id: uuid.UUID = Field(sa_column=Column(ForeignKey("sheets.id", ondelete="CASCADE")))
    session_id: Optional[uuid.UUID] = Field(default=None, sa_column=Column(ForeignKey("chat_sessions.id", ondelete="SET NULL")))
    message_id: Optional[uuid.UUID] = Field(default=None)
    job_type: str = Field(max_length=100, nullable=False)
    target_range: str = Field(nullable=False)
    status: str = Field(max_length=30, default="pending")
    progress: float = Field(default=0.0)
    payload: Optional[Dict] = Field(default=None, sa_column=Column(JSONB))
    result: Optional[Dict] = Field(default=None, sa_column=Column(JSONB))
    error_message: Optional[str] = Field(default=None)
    started_at: Optional[datetime] = Field(default=None)
    completed_at: Optional[datetime] = Field(default=None)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
