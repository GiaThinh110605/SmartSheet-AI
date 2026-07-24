from datetime import datetime
from typing import List, Optional
from uuid import UUID
from sqlmodel import select
from fastapi import APIRouter, Depends, HTTPException, status
from app.core.dependency import get_current_user
from app.db.session import SessionDep
from app.schemas.sheet import SheetCreate, SheetOut, SheetUpdate, SheetDataResponse, SheetBatchUpdate, CellChange
from app.schemas.cell import CellOut
from app.models.sheet import Sheet
from app.models.cell import Cell
from app.models.column import SheetColumn
from app.models.sheet_asset import SheetAsset
from app.models.workbook import Workbook
from app.models.user import User

router = APIRouter(prefix="", tags=["sheets"])

@router.post("/workbooks/{workbook_id}/sheets", response_model=SheetOut, status_code=status.HTTP_201_CREATED)
@router.post("/sheets", response_model=SheetOut, status_code=status.HTTP_201_CREATED)
def create_sheet(workbook_id: UUID | None = None, payload: SheetCreate | None = None, db: SessionDep = None, current_user: User = Depends(get_current_user)):
    if payload is None:
        raise HTTPException(status_code=422, detail="Payload is required")
    if workbook_id is None:
        raise HTTPException(status_code=422, detail="Workbook ID is required")
    workbook = db.get(Workbook, workbook_id)
    if not workbook or workbook.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Workbook not found or unauthorized")
    sheet = Sheet(
        workbook_id=workbook_id,
        name=payload.name,
        index=payload.index,
        data=payload.data or {}
    )
    db.add(sheet)
    db.commit()
    db.refresh(sheet)
    return sheet

@router.get("/sheets/{sheet_id}", response_model=SheetOut)
@router.get("/{sheet_id}", response_model=SheetOut)
def get_sheet(sheet_id: UUID, db: SessionDep, current_user: User = Depends(get_current_user)):
    sheet = db.get(Sheet, sheet_id)
    if not sheet:
        raise HTTPException(status_code=404, detail="Sheet not found")
    workbook = db.get(Workbook, sheet.workbook_id)
    if not workbook or workbook.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Sheet not found or unauthorized")
    return sheet

@router.patch("/sheets/{sheet_id}", response_model=SheetOut)
@router.patch("/{sheet_id}", response_model=SheetOut)
def update_sheet(sheet_id: UUID, payload: SheetUpdate, db: SessionDep, current_user: User = Depends(get_current_user)):
    sheet = db.get(Sheet, sheet_id)
    if not sheet:
        raise HTTPException(status_code=404, detail="Sheet not found")
    workbook = db.get(Workbook, sheet.workbook_id)
    if not workbook or workbook.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Sheet not found or unauthorized")
    sheet_data = payload.model_dump(exclude_unset=True)
    for key, value in sheet_data.items():
        setattr(sheet, key, value)
    sheet.updated_at = datetime.utcnow()
    db.add(sheet)
    db.commit()
    db.refresh(sheet)
    return sheet

@router.delete("/sheets/{sheet_id}", status_code=status.HTTP_204_NO_CONTENT)
@router.delete("/{sheet_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sheet(sheet_id: UUID, db: SessionDep, current_user: User = Depends(get_current_user)):
    sheet = db.get(Sheet, sheet_id)
    if not sheet:
        raise HTTPException(status_code=404, detail="Sheet not found")
    workbook = db.get(Workbook, sheet.workbook_id)
    if not workbook or workbook.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Sheet not found or unauthorized")
    db.delete(sheet)
    db.commit()
    return None

@router.get("/sheets/{sheet_id}/data", response_model=SheetDataResponse)
@router.get("/{sheet_id}/data", response_model=SheetDataResponse)
def load_sheet_data(sheet_id: UUID, db: SessionDep, current_user: User = Depends(get_current_user)):
    sheet = db.get(Sheet, sheet_id)
    if not sheet:
        raise HTTPException(status_code=404, detail="Sheet not found")
    workbook = db.get(Workbook, sheet.workbook_id)
    if not workbook or workbook.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Sheet not found or unauthorized")
    return {
        "data": sheet.data or [],
        "version": sheet.version
    }

@router.put("/sheets/{sheet_id}/cells", response_model=List[CellOut])
@router.put("/{sheet_id}/cells", response_model=List[CellOut])
def save_cells(sheet_id: UUID, changes: List[CellChange], db: SessionDep, current_user: User = Depends(get_current_user)):
    sheet = db.get(Sheet, sheet_id)
    if not sheet:
        raise HTTPException(status_code=404, detail="Sheet not found")
    workbook = db.get(Workbook, sheet.workbook_id)
    if not workbook or workbook.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Sheet not found or unauthorized")

    saved_cells = []
    for change in changes:
        statement = select(Cell).where(
            Cell.sheet_id == sheet_id,
            Cell.row_index == change.row_index,
            Cell.col_index == change.col_index
        )
        cell = db.exec(statement).first()
        if cell:
            cell.value = change.value
            cell.updated_at = datetime.utcnow()
            cell.version += 1
        else:
            cell = Cell(
                sheet_id=sheet_id,
                row_index=change.row_index,
                col_index=change.col_index,
                value=change.value,
                version=1
            )
            db.add(cell)
        db.commit()
        db.refresh(cell)
        saved_cells.append(cell)

    sheet.version += 1
    sheet.updated_at = datetime.utcnow()
    db.add(sheet)
    db.commit()
    return saved_cells

@router.patch("/sheets/{sheet_id}/rows", response_model=SheetDataResponse)
@router.patch("/{sheet_id}/rows", response_model=SheetDataResponse)
def batch_update_rows(sheet_id: UUID, payload: SheetBatchUpdate, db: SessionDep, current_user: User = Depends(get_current_user)):
    sheet = db.get(Sheet, sheet_id)
    if not sheet:
        raise HTTPException(status_code=404, detail="Sheet not found")
    workbook = db.get(Workbook, sheet.workbook_id)
    if not workbook or workbook.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Sheet not found or unauthorized")

    data = sheet.data or []
    for row_item in payload.rows:
        row_index = row_item.get("row_index")
        if row_index is None or row_index < 0:
            continue
        if row_index < len(data):
            data[row_index].update(row_item.get("values", {}))
        else:
            data.append(row_item.get("values", {}))

    sheet.data = data
    sheet.version += 1
    sheet.updated_at = datetime.utcnow()
    db.add(sheet)
    db.commit()
    db.refresh(sheet)
    return {"data": sheet.data or [], "version": sheet.version}

@router.post("/{sheet_id}/undo", status_code=status.HTTP_200_OK)
def undo(sheet_id: UUID, db: SessionDep, current_user: User = Depends(get_current_user)):
    raise HTTPException(status_code=501, detail="Undo is not implemented yet")

@router.post("/{sheet_id}/redo", status_code=status.HTTP_200_OK)
def redo(sheet_id: UUID, db: SessionDep, current_user: User = Depends(get_current_user)):
    raise HTTPException(status_code=501, detail="Redo is not implemented yet")
