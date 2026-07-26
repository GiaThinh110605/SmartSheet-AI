from datetime import datetime
from typing import Dict, Optional, List
from uuid import UUID
from pydantic import BaseModel

class AIJobCreate(BaseModel):
    sheet_id: UUID
    job_type: str
    target_range: str
    payload: Optional[Dict] = None
    session_id: Optional[UUID] = None
    message_id: Optional[UUID] = None

class AIJobOut(BaseModel):
    id: UUID
    sheet_id: UUID
    session_id: Optional[UUID]
    message_id: Optional[UUID]
    job_type: str
    target_range: str
    status: str
    progress: float
    payload: Optional[Dict]
    result: Optional[Dict]
    error_message: Optional[str]
    started_at: Optional[datetime]
    completed_at: Optional[datetime]
    created_at: datetime

    class Config:
        from_attributes = True

class AIJobUpdate(BaseModel):
    status: Optional[str] = None
    progress: Optional[float] = None
    result: Optional[Dict] = None
    error_message: Optional[str] = None

class AIJobPreviewOut(BaseModel):
    job_id: UUID
    preview: Dict
    status: str

class AIJobCommitRequest(BaseModel):
    action: str

class AIChatToSheetRequest(BaseModel):
    sheet_id: UUID
    prompt: str

class AIBulkCleanRequest(BaseModel):
    sheet_id: UUID
    col_index: int
    clean_type: str

class AICustomFunctionRequest(BaseModel):
    sheet_id: UUID
    function_type: str
    cells_range: str
    args: Optional[List[str]] = None

class AINLQueryRequest(BaseModel):
    sheet_id: UUID
    question: str

class AINLChartRequest(BaseModel):
    sheet_id: UUID
    prompt: str
