from datetime import datetime
from typing import List, Optional
from uuid import UUID
from sqlmodel import select
from fastapi import APIRouter, Depends, HTTPException, status
from app.core.dependency import get_current_user
from app.db.session import SessionDep
from app.schemas.ai import AIJobCreate, AIJobOut, AIJobUpdate
from app.models.ai_job import AIJob
from app.models.sheet import Sheet
from app.models.chat_session import ChatSession
from app.models.user import User
from app.models.workbook import Workbook

router = APIRouter(prefix="/ai", tags=["ai"])

@router.post("/jobs", response_model=AIJobOut, status_code=status.HTTP_201_CREATED)
def create_ai_job(payload: AIJobCreate, db: SessionDep, current_user: User = Depends(get_current_user)):
    sheet = db.get(Sheet, payload.sheet_id)
    if not sheet:
        raise HTTPException(status_code=404, detail="Sheet not found")
    workbook = db.get(Workbook, sheet.workbook_id)
    if not workbook or workbook.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Sheet not found or unauthorized")
    session = None
    if payload.session_id:
        session = db.get(ChatSession, payload.session_id)
        if not session or session.user_id != current_user.id:
            raise HTTPException(status_code=404, detail="Chat session not found or unauthorized")
    job = AIJob(
        sheet_id=payload.sheet_id,
        session_id=payload.session_id if hasattr(payload, "session_id") else None,
        message_id=getattr(payload, "message_id", None),
        job_type=payload.job_type,
        target_range=payload.target_range,
        payload=payload.payload,
        status="pending",
        progress=0.0,
        created_at=datetime.utcnow(),
    )
    db.add(job)
    db.commit()
    db.refresh(job)
    return job

@router.get("/jobs", response_model=List[AIJobOut])
def list_ai_jobs(db: SessionDep, current_user: User = Depends(get_current_user)):
    statement = select(AIJob).where(AIJob.id != None)
    return db.exec(statement).all()

@router.get("/jobs/{job_id}", response_model=AIJobOut)
def get_ai_job(job_id: UUID, db: SessionDep, current_user: User = Depends(get_current_user)):
    job = db.get(AIJob, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="AI job not found")
    sheet = db.get(Sheet, job.sheet_id)
    workbook = db.get(Workbook, sheet.workbook_id)
    if not workbook or workbook.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="AI job not found or unauthorized")
    return job

@router.post("/jobs/{job_id}/retry", response_model=AIJobOut)
def retry_ai_job(job_id: UUID, db: SessionDep, current_user: User = Depends(get_current_user)):
    job = db.get(AIJob, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="AI job not found")
    sheet = db.get(Sheet, job.sheet_id)
    workbook = db.get(Workbook, sheet.workbook_id)
    if not workbook or workbook.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="AI job not found or unauthorized")
    job.status = "pending"
    job.progress = 0.0
    job.error_message = None
    job.started_at = None
    job.completed_at = None
    db.add(job)
    db.commit()
    db.refresh(job)
    return job

@router.post("/jobs/{job_id}/cancel", response_model=AIJobOut)
def cancel_ai_job(job_id: UUID, db: SessionDep, current_user: User = Depends(get_current_user)):
    job = db.get(AIJob, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="AI job not found")
    sheet = db.get(Sheet, job.sheet_id)
    workbook = db.get(Workbook, sheet.workbook_id)
    if not workbook or workbook.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="AI job not found or unauthorized")
    job.status = "cancelled"
    job.progress = 0.0
    job.completed_at = datetime.utcnow()
    db.add(job)
    db.commit()
    db.refresh(job)
    return job
