from datetime import datetime
from typing import List
from uuid import UUID
from sqlmodel import select
from fastapi import APIRouter, Depends, HTTPException, status
from app.core.dependency import get_current_user
from app.db.session import SessionDep
from app.schemas.column import ColumnCreate, ColumnOut, ColumnUpdate
from app.models.sheet import Sheet
from app.models.column import SheetColumn
from app.models.user import User
from app.models.workbook import Workbook

router = APIRouter(prefix="", tags=["columns"])

@router.post("/sheets/{sheet_id}/columns", response_model=ColumnOut, status_code=status.HTTP_201_CREATED)
@router.post("/columns", response_model=ColumnOut, status_code=status.HTTP_201_CREATED)
def create_column(sheet_id: UUID | None = None, payload: ColumnCreate | None = None, db: SessionDep = None, current_user: User = Depends(get_current_user)):
    if payload is None:
        raise HTTPException(status_code=422, detail="Payload is required")
    if sheet_id is None:
        raise HTTPException(status_code=422, detail="Sheet ID is required")
    sheet = db.get(Sheet, sheet_id)
    if not sheet:
        raise HTTPException(status_code=404, detail="Sheet not found")
    workbook = db.get(Workbook, sheet.workbook_id)
    if not workbook or workbook.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Sheet not found or unauthorized")

    column = SheetColumn(
        sheet_id=sheet_id,
        col_index=payload.col_index,
        name=payload.name,
        data_type=payload.data_type,
        format_options=payload.format_options,
        is_required=payload.is_required,
        default_value=payload.default_value,
    )
    db.add(column)
    db.commit()
    db.refresh(column)
    return column

@router.get("/sheets/{sheet_id}/columns", response_model=List[ColumnOut])
@router.get("/columns", response_model=List[ColumnOut])
def list_columns(sheet_id: UUID | None = None, db: SessionDep = None, current_user: User = Depends(get_current_user)):
    if sheet_id is None:
        raise HTTPException(status_code=422, detail="Sheet ID is required")
    sheet = db.get(Sheet, sheet_id)
    if not sheet:
        raise HTTPException(status_code=404, detail="Sheet not found")
    workbook = db.get(Workbook, sheet.workbook_id)
    if not workbook or workbook.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Sheet not found or unauthorized")
    statement = select(SheetColumn).where(SheetColumn.sheet_id == sheet_id)
    return db.exec(statement).all()

@router.patch("/columns/{column_id}", response_model=ColumnOut)
@router.patch("/{column_id}", response_model=ColumnOut)
def update_column(column_id: UUID, payload: ColumnUpdate, db: SessionDep, current_user: User = Depends(get_current_user)):
    column = db.get(SheetColumn, column_id)
    if not column:
        raise HTTPException(status_code=404, detail="Column not found")
    sheet = db.get(Sheet, column.sheet_id)
    workbook = db.get(Workbook, sheet.workbook_id)
    if not workbook or workbook.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Column not found or unauthorized")

    column_data = payload.model_dump(exclude_unset=True)
    for key, value in column_data.items():
        setattr(column, key, value)
    column.updated_at = datetime.utcnow()
    db.add(column)
    db.commit()
    db.refresh(column)
    return column

@router.delete("/columns/{column_id}", status_code=status.HTTP_204_NO_CONTENT)
@router.delete("/{column_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_column(column_id: UUID, db: SessionDep, current_user: User = Depends(get_current_user)):
    column = db.get(SheetColumn, column_id)
    if not column:
        raise HTTPException(status_code=404, detail="Column not found")
    sheet = db.get(Sheet, column.sheet_id)
    workbook = db.get(Workbook, sheet.workbook_id)
    if not workbook or workbook.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Column not found or unauthorized")
    db.delete(column)
    db.commit()
    return None
