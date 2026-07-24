from datetime import datetime
from typing import List, Optional
from uuid import UUID
from sqlmodel import select
from fastapi import APIRouter, Depends, HTTPException, status
from app.core.dependency import get_current_user
from app.db.session import SessionDep
from app.schemas.chat import ChatSessionCreate, ChatSessionOut, ChatMessageCreate, ChatMessageOut, ChatSessionMessagesOut
from app.models.chat_session import ChatSession
from app.models.chat_message import ChatMessage
from app.models.sheet import Sheet
from app.models.user import User
from app.models.workbook import Workbook

router = APIRouter(prefix="/chat/sessions", tags=["chat"])

@router.post("", response_model=ChatSessionOut, status_code=status.HTTP_201_CREATED)
def create_chat_session(payload: ChatSessionCreate, db: SessionDep, current_user: User = Depends(get_current_user)):
    sheet = None
    if payload.sheet_id:
        sheet = db.get(Sheet, payload.sheet_id)
        if not sheet:
            raise HTTPException(status_code=404, detail="Sheet not found")
        workbook = db.get(Workbook, sheet.workbook_id)
        if not workbook or workbook.user_id != current_user.id:
            raise HTTPException(status_code=404, detail="Sheet not found or unauthorized")
    session = ChatSession(
        sheet_id=payload.sheet_id,
        user_id=current_user.id,
        title=payload.title or "Phiên chat mới",
        last_active=datetime.utcnow(),
    )
    db.add(session)
    db.commit()
    db.refresh(session)
    return session

@router.get("", response_model=List[ChatSessionOut])
def list_chat_sessions(db: SessionDep, current_user: User = Depends(get_current_user)):
    statement = select(ChatSession).where(ChatSession.user_id == current_user.id)
    return db.exec(statement).all()

@router.get("/{session_id}", response_model=ChatSessionOut)
def get_chat_session(session_id: UUID, db: SessionDep, current_user: User = Depends(get_current_user)):
    session = db.get(ChatSession, session_id)
    if not session or session.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Chat session not found")
    return session

@router.delete("/{session_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_chat_session(session_id: UUID, db: SessionDep, current_user: User = Depends(get_current_user)):
    session = db.get(ChatSession, session_id)
    if not session or session.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Chat session not found")
    db.delete(session)
    db.commit()
    return None

@router.post("/{session_id}/messages", response_model=ChatMessageOut, status_code=status.HTTP_201_CREATED)
def send_message(session_id: UUID, payload: ChatMessageCreate, db: SessionDep, current_user: User = Depends(get_current_user)):
    session = db.get(ChatSession, session_id)
    if not session or session.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Chat session not found")
    if session_id != payload.session_id:
        raise HTTPException(status_code=400, detail="Session ID mismatch")
    message = ChatMessage(
        session_id=payload.session_id,
        user_id=current_user.id,
        role=payload.role,
        content=payload.content,
        meta=getattr(payload, "meta", None),
    )
    db.add(message)
    db.commit()
    db.refresh(message)
    session.last_active = datetime.utcnow()
    db.add(session)
    db.commit()
    return message

@router.get("/{session_id}/messages", response_model=List[ChatMessageOut])
def get_messages(session_id: UUID, db: SessionDep, current_user: User = Depends(get_current_user)):
    session = db.get(ChatSession, session_id)
    if not session or session.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Chat session not found")
    statement = select(ChatMessage).where(ChatMessage.session_id == session_id).order_by(ChatMessage.created_at)
    return db.exec(statement).all()
