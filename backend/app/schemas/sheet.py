from datetime import datetime
from typing import Dict, List, Optional
from uuid import UUID
from pydantic import BaseModel

class SheetCreate(BaseModel):
    name: str
    index: Optional[int] = 0
    data: Optional[Dict] = None

class SheetUpdate(BaseModel):
    name: Optional[str] = None
    index: Optional[int] = None
    data: Optional[Dict] = None
    last_synced_at: Optional[datetime] = None
    version: Optional[int] = None

class SheetOut(BaseModel):
    id: UUID
    workbook_id: UUID
    name: str
    index: int
    data: Optional[Dict]
    last_synced_at: datetime
    version: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class CellChange(BaseModel):
    row_index: int
    col_index: int
    value: Optional[str] = None

class SheetDataResponse(BaseModel):
    data: List[Dict]
    version: int

class SheetBatchUpdate(BaseModel):
    rows: List[Dict]

class SheetSortRequest(BaseModel):
    col_index: int
    order: str = "asc"

class SheetFilterRequest(BaseModel):
    filters: Dict

class SheetRemoveDuplicatesRequest(BaseModel):
    key_columns: List[int]

class SheetSearchRequest(BaseModel):
    query: str

class SheetReplaceRequest(BaseModel):
    search: str
    replace: str

class SheetImportResponse(BaseModel):
    success: bool
    rows_imported: int
    message: Optional[str] = None

class SheetExportResponse(BaseModel):
    success: bool
    file_url: Optional[str] = None
    message: Optional[str] = None
