from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
import uuid
from typing import Optional, Dict
from sqlmodel import SQLModel, Field
from datetime import datetime, timezone

class ChatMessage(SQLModel, table=True):
    __tablename__ = "chat_messages"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, nullable=False, index=True)
    session_id: uuid.UUID = Field(sa_column=Column(ForeignKey("chat_sessions.id", ondelete="CASCADE")))
    user_id: uuid.UUID = Field(sa_column=Column(ForeignKey("users.id", ondelete="CASCADE")))
    role: str = Field(max_length=20, nullable=False)
    content: str = Field(nullable=False)
    meta: Optional[Dict] = Field(default=None, sa_column=Column('metadata', JSONB))
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
