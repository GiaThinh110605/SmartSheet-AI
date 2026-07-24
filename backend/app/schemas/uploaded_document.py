from datetime import datetime
from typing import Dict, Optional
from uuid import UUID
from pydantic import BaseModel

class UploadDocumentOut(BaseModel):
    id: UUID
    user_id: UUID
    sheet_id: UUID
    file_name: str
    file_url: Optional[str]
    file_type: str
    ocr_result: Optional[Dict]
    processed_status: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True

class AuditLogOut(BaseModel):
    id: UUID
    user_id: UUID
    sheet_id: UUID
    action: str
    details: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True
