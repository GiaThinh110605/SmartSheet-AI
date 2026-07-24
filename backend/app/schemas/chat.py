from datetime import datetime
from typing import Dict, Optional, List
from uuid import UUID
from pydantic import BaseModel

class ChatSessionCreate(BaseModel):
    sheet_id: Optional[UUID] = None
    title: Optional[str] = None

class ChatSessionOut(BaseModel):
    id: UUID
    sheet_id: Optional[UUID]
    user_id: UUID
    title: Optional[str]
    started_at: datetime
    last_active: datetime
    context_snapshot: Optional[Dict]

    class Config:
        from_attributes = True

class ChatMessageCreate(BaseModel):
    session_id: UUID
    role: str
    content: str
    meta: Optional[Dict] = None

class ChatMessageOut(BaseModel):
    id: UUID
    session_id: UUID
    user_id: UUID
    role: str
    content: str
    meta: Optional[Dict]
    created_at: datetime

    class Config:
        from_attributes = True

class ChatSessionMessagesOut(BaseModel):
    session: ChatSessionOut
    messages: List[ChatMessageOut]
