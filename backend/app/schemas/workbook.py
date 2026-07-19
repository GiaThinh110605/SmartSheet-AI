
from uuid import UUID
from typing import Dict
from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class WorkbookCreate(BaseModel):
    name: str
    description: Optional[str] = None
    meta_data: Optional[Dict] = None

class WorkbookUdpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    meta_data: Optional[Dict] = None

class WorkbookOut(BaseModel):
    id: UUID
    user_id: UUID
    name: str
    description: Optional[str]
    is_active: bool
    meta_data: Optional[Dict]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True       
    