
from uuid import UUID
from fastapi import HTTPException
from starlette.status import HTTP_404_NOT_FOUND
from sqlmodel import select
from app.core.dependency import get_current_user
from fastapi import Depends
from app.db.session import SessionDep
from app.schemas.workbook import WorkbookCreate
from fastapi import APIRouter
from app.schemas.workbook import WorkbookOut, WorkbookUdpdate
from fastapi import status
from app.models.user import User
from app.models.workbook import Workbook
from typing import List
from datetime import datetime


router = APIRouter(prefix="/workbooks", tags=["workbooks"])

@router.post("", response_model=WorkbookOut, status_code=status.HTTP_201_CREATED)
def created_workbook(
    payload: WorkbookCreate,
    db: SessionDep,
    current_user: User = Depends(get_current_user)
):
    db_workbook = Workbook(
        user_id=current_user.id,
        name=payload.name,
        description=payload.description,
        meta_data=payload.meta_data if payload.meta_data else {}
    )
    db.add(db_workbook)
    db.commit()
    db.refresh(db_workbook)
    return db_workbook

@router.get("", response_model=List[WorkbookOut])
def get_all_workbook(db: SessionDep, current_user: User = Depends(get_current_user)):
    statement = select(Workbook).where(Workbook.user_id == current_user.id)
    workbook = db.exec(statement).all()

    if not workbook:
        raise HTTPException(status_code=404, detail="Workbook not found or unauthorized")
    return workbook

@router.get("/{id}", response_model=WorkbookOut)
def get_workbook_by_id(
    id: UUID,
    db:SessionDep,
    current_user: User = Depends(get_current_user)
):
    statement = select(Workbook).where(
        Workbook.user_id == current_user.id,
        Workbook.id == id
    )
    workbook = db.exec(statement).first()
    if not workbook:
        raise HTTPException(status_code=404, detail="Workbook not found or unauthorized")
    return workbook

@router.patch("/{id}", response_model=WorkbookOut)
def update_workbook(
    id: UUID,
    payload: WorkbookUdpdate,
    db: SessionDep,
    current_user: User = Depends(get_current_user)
):
    statement = select(Workbook).where(
        Workbook.id == id,
        Workbook.user_id == current_user.id
    )
    workbook = db.exec(statement).first()
    if not workbook:
        raise HTTPException(status_code=404, detail="Workbook not found or unauthorized")
    
    workbook_data = payload.model_dump(exclude_unset=True)
    for key, value in workbook_data.items():
        setattr(workbook, key, value)
    workbook.updated_at = datetime.utcnow()
    
    db.add(workbook)
    db.commit()
    db.refresh(workbook)
    return workbook

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_workbook(
    id: UUID,
    db: SessionDep,
    current_user: User = Depends(get_current_user)
):
    statement = select(Workbook).where(
        Workbook.id == id,
        Workbook.user_id == current_user.id
    )
    workbook = db.exec(statement).first()
    
    if not workbook:
        raise HTTPException(status_code=404, detail="Workbook not found or unauthorized")
    db.delete(workbook)
    db.commit()
    return None