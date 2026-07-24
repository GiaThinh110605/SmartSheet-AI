from sqlalchemy import Column, ForeignKey
import uuid
from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime, timezone

class AuditLog(SQLModel, table=True):
    __tablename__ = "audit_logs"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, nullable=False, index=True)
    user_id: uuid.UUID = Field(sa_column=Column(ForeignKey("users.id", ondelete="CASCADE")))
    sheet_id: uuid.UUID = Field(sa_column=Column(ForeignKey("sheets.id", ondelete="CASCADE")))
    action: str = Field(max_length=100, nullable=False)
    details: Optional[str] = Field(default=None)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
