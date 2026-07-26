from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel

class CellOut(BaseModel):
    id: UUID
    sheet_id: UUID
    row_index: int
    col_index: int
    value: Optional[str]
    computed_value: Optional[str]
    status: Optional[str]
    version: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class CellCreate(BaseModel):
    sheet_id: UUID
    row_index: int
    col_index: int
    value: Optional[str] = None

class CellUpdate(BaseModel):
    value: Optional[str] = None
    computed_value: Optional[str] = None
    status: Optional[str] = None
    version: Optional[int] = None
