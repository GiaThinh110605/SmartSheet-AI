from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
import uuid
from typing import Optional, Dict
from sqlmodel import SQLModel, Field
from datetime import datetime, timezone

class SheetAsset(SQLModel, table=True):
    __tablename__ = "sheet_assets"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, nullable=False, index=True)
    sheet_id: uuid.UUID = Field(sa_column=Column(ForeignKey("sheets.id", ondelete="CASCADE")))
    asset_type: str = Field(max_length=50, nullable=False)
    position_config: Optional[Dict] = Field(default=None, sa_column=Column(JSONB))
    data_config: Optional[Dict] = Field(default=None, sa_column=Column(JSONB))
    layer_order: int = Field(default=0)
    created_by: Optional[uuid.UUID] = Field(default=None)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
