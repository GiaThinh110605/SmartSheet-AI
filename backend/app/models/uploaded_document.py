from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
import uuid
from typing import Optional, Dict
from sqlmodel import SQLModel, Field
from datetime import datetime, timezone

class UploadedDocument(SQLModel, table=True):
    __tablename__ = "uploaded_documents"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, nullable=False, index=True)
    user_id: uuid.UUID = Field(sa_column=Column(ForeignKey("users.id", ondelete="CASCADE")))
    sheet_id: uuid.UUID = Field(sa_column=Column(ForeignKey("sheets.id", ondelete="CASCADE")))
    file_name: str = Field(max_length=255, nullable=False)
    file_url: Optional[str] = Field(default=None)
    file_type: str = Field(max_length=100, nullable=False)
    ocr_result: Optional[Dict] = Field(default=None, sa_column=Column(JSONB))
    processed_status: Optional[str] = Field(default=None, max_length=50)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
