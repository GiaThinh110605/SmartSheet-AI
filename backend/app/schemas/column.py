from datetime import datetime
from typing import Dict, Optional
from uuid import UUID
from pydantic import BaseModel

class ColumnCreate(BaseModel):
    col_index: int
    name: str
    data_type: str
    format_options: Optional[Dict] = None
    is_required: Optional[bool] = False
    default_value: Optional[str] = None

class ColumnUpdate(BaseModel):
    col_index: Optional[int] = None
    name: Optional[str] = None
    data_type: Optional[str] = None
    format_options: Optional[Dict] = None
    is_required: Optional[bool] = None
    default_value: Optional[str] = None

class ColumnOut(BaseModel):
    id: UUID
    sheet_id: UUID
    col_index: int
    name: str
    data_type: str
    format_options: Optional[Dict]
    is_required: bool
    default_value: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
