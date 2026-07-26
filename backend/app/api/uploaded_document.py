from datetime import datetime
from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, File, UploadFile, HTTPException, status
from sqlmodel import select
from app.core.dependency import get_current_user
from app.db.session import SessionDep
from app.schemas.uploaded_document import UploadDocumentOut, AuditLogOut
from app.models.uploaded_document import UploadedDocument
from app.models.audit_log import AuditLog
from app.models.sheet import Sheet
from app.models.user import User
from app.models.workbook import Workbook

router = APIRouter(prefix="/uploaded-documents", tags=["uploaded-documents"])

@router.get("/{document_id}", response_model=UploadDocumentOut)
def get_uploaded_document(document_id: UUID, db: SessionDep, current_user: User = Depends(get_current_user)):
    document = db.get(UploadedDocument, document_id)
    if not document or document.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Document not found")
    return document

@router.delete("/{document_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_uploaded_document(document_id: UUID, db: SessionDep, current_user: User = Depends(get_current_user)):
    document = db.get(UploadedDocument, document_id)
    if not document or document.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Document not found")
    db.delete(document)
    db.commit()
    return None

@router.get("/sheet/{sheet_id}/audit-logs", response_model=List[AuditLogOut])
def list_audit_logs(sheet_id: UUID, db: SessionDep, current_user: User = Depends(get_current_user)):
    sheet = db.get(Sheet, sheet_id)
    if not sheet:
        raise HTTPException(status_code=404, detail="Sheet not found")
    workbook = db.get(Workbook, sheet.workbook_id)
    if not workbook or workbook.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Sheet not found or unauthorized")
    statement = select(AuditLog).where(AuditLog.sheet_id == sheet_id)
    return db.exec(statement).all()
