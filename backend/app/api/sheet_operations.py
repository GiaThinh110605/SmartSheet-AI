from datetime import datetime
from typing import List, Dict, Optional
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from sqlmodel import select
from app.core.dependency import get_current_user
from app.db.session import SessionDep
from app.schemas.sheet import SheetDataResponse, SheetBatchUpdate, SheetSortRequest, SheetFilterRequest, SheetRemoveDuplicatesRequest, SheetSearchRequest, SheetReplaceRequest, SheetImportResponse, SheetExportResponse
from app.models.sheet import Sheet
from app.models.workbook import Workbook
from app.models.user import User

router = APIRouter(prefix="/sheets", tags=["sheets"])

@router.post("/{sheet_id}/sort", response_model=SheetDataResponse)
def sort_sheet(sheet_id: UUID, payload: SheetSortRequest, db: SessionDep, current_user: User = Depends(get_current_user)):
    sheet = db.get(Sheet, sheet_id)
    if not sheet:
        raise HTTPException(status_code=404, detail="Sheet not found")
    workbook = db.get(Workbook, sheet.workbook_id)
    if not workbook or workbook.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Sheet not found or unauthorized")
    data = sheet.data or []
    try:
        data.sort(key=lambda row: row.get(str(payload.col_index), ""), reverse=payload.order != "asc")
    except Exception:
        pass
    sheet.data = data
    sheet.version += 1
    sheet.updated_at = datetime.utcnow()
    db.add(sheet)
    db.commit()
    db.refresh(sheet)
    return {"data": sheet.data or [], "version": sheet.version}

@router.post("/{sheet_id}/filter", response_model=SheetDataResponse)
def filter_sheet(sheet_id: UUID, payload: SheetFilterRequest, db: SessionDep, current_user: User = Depends(get_current_user)):
    sheet = db.get(Sheet, sheet_id)
    if not sheet:
        raise HTTPException(status_code=404, detail="Sheet not found")
    workbook = db.get(Workbook, sheet.workbook_id)
    if not workbook or workbook.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Sheet not found or unauthorized")
    data = sheet.data or []
    filters = payload.filters or {}
    filtered = [row for row in data if all(str(row.get(k, "")).lower() == str(v).lower() for k, v in filters.items())]
    return {"data": filtered, "version": sheet.version}

@router.post("/{sheet_id}/remove-duplicates", response_model=SheetDataResponse)
def remove_duplicates(sheet_id: UUID, payload: SheetRemoveDuplicatesRequest, db: SessionDep, current_user: User = Depends(get_current_user)):
    sheet = db.get(Sheet, sheet_id)
    if not sheet:
        raise HTTPException(status_code=404, detail="Sheet not found")
    workbook = db.get(Workbook, sheet.workbook_id)
    if not workbook or workbook.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Sheet not found or unauthorized")
    data = sheet.data or []
    seen = set()
    unique = []
    for row in data:
        key = tuple(row.get(str(idx), None) for idx in payload.key_columns)
        if key not in seen:
            seen.add(key)
            unique.append(row)
    sheet.data = unique
    sheet.version += 1
    sheet.updated_at = datetime.utcnow()
    db.add(sheet)
    db.commit()
    db.refresh(sheet)
    return {"data": sheet.data or [], "version": sheet.version}

@router.post("/{sheet_id}/search", response_model=SheetDataResponse)
def search_sheet(sheet_id: UUID, payload: SheetSearchRequest, db: SessionDep, current_user: User = Depends(get_current_user)):
    sheet = db.get(Sheet, sheet_id)
    if not sheet:
        raise HTTPException(status_code=404, detail="Sheet not found")
    workbook = db.get(Workbook, sheet.workbook_id)
    if not workbook or workbook.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Sheet not found or unauthorized")
    data = sheet.data or []
    matches = [row for row in data if any(payload.query.lower() in str(value).lower() for value in row.values())]
    return {"data": matches, "version": sheet.version}

@router.post("/{sheet_id}/replace", response_model=SheetDataResponse)
def replace_sheet(sheet_id: UUID, payload: SheetReplaceRequest, db: SessionDep, current_user: User = Depends(get_current_user)):
    sheet = db.get(Sheet, sheet_id)
    if not sheet:
        raise HTTPException(status_code=404, detail="Sheet not found")
    workbook = db.get(Workbook, sheet.workbook_id)
    if not workbook or workbook.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Sheet not found or unauthorized")
    data = sheet.data or []
    changed = False
    for row in data:
        for key, value in row.items():
            if isinstance(value, str) and payload.search in value:
                row[key] = value.replace(payload.search, payload.replace)
                changed = True
    if changed:
        sheet.data = data
        sheet.version += 1
        sheet.updated_at = datetime.utcnow()
        db.add(sheet)
        db.commit()
        db.refresh(sheet)
    return {"data": sheet.data or [], "version": sheet.version}

@router.post("/{sheet_id}/import", response_model=SheetImportResponse)
def import_sheet(sheet_id: UUID, file: UploadFile = File(...), db: SessionDep = Depends(get_db), current_user: User = Depends(get_current_user)):
    return {"success": True, "rows_imported": 0, "message": "Import not implemented"}

@router.get("/{sheet_id}/export", response_model=SheetExportResponse)
def export_sheet(sheet_id: UUID, db: SessionDep, current_user: User = Depends(get_current_user)):
    return {"success": True, "file_url": None, "message": "Export not implemented"}
