from datetime import datetime
from typing import List
from uuid import UUID
from sqlmodel import select
from fastapi import APIRouter, Depends, HTTPException, status
from app.core.dependency import get_current_user
from app.db.session import SessionDep
from app.schemas.sheet_asset import SheetAssetCreate, SheetAssetOut, SheetAssetUpdate
from app.models.sheet import Sheet
from app.models.sheet_asset import SheetAsset
from app.models.user import User
from app.models.workbook import Workbook

router = APIRouter(prefix="", tags=["assets"])

@router.post("/sheets/{sheet_id}/assets", response_model=SheetAssetOut, status_code=status.HTTP_201_CREATED)
@router.post("/assets", response_model=SheetAssetOut, status_code=status.HTTP_201_CREATED)
def create_asset(sheet_id: UUID | None = None, payload: SheetAssetCreate | None = None, db: SessionDep = None, current_user: User = Depends(get_current_user)):
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
    asset = SheetAsset(
        sheet_id=sheet_id,
        asset_type=payload.asset_type,
        position_config=payload.position_config,
        data_config=payload.data_config,
        layer_order=payload.layer_order,
        created_by=payload.created_by,
    )
    db.add(asset)
    db.commit()
    db.refresh(asset)
    return asset

@router.get("/sheets/{sheet_id}/assets", response_model=List[SheetAssetOut])
@router.get("/sheet/{sheet_id}", response_model=List[SheetAssetOut])
def list_assets(sheet_id: UUID, db: SessionDep, current_user: User = Depends(get_current_user)):
    sheet = db.get(Sheet, sheet_id)
    if not sheet:
        raise HTTPException(status_code=404, detail="Sheet not found")
    workbook = db.get(Workbook, sheet.workbook_id)
    if not workbook or workbook.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Sheet not found or unauthorized")
    statement = select(SheetAsset).where(SheetAsset.sheet_id == sheet_id)
    return db.exec(statement).all()

@router.patch("/assets/{asset_id}", response_model=SheetAssetOut)
@router.patch("/{asset_id}", response_model=SheetAssetOut)
def update_asset(asset_id: UUID, payload: SheetAssetUpdate, db: SessionDep, current_user: User = Depends(get_current_user)):
    asset = db.get(SheetAsset, asset_id)
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    sheet = db.get(Sheet, asset.sheet_id)
    workbook = db.get(Workbook, sheet.workbook_id)
    if not workbook or workbook.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Asset not found or unauthorized")
    asset_data = payload.model_dump(exclude_unset=True)
    for key, value in asset_data.items():
        setattr(asset, key, value)
    asset.updated_at = datetime.utcnow()
    db.add(asset)
    db.commit()
    db.refresh(asset)
    return asset

@router.delete("/assets/{asset_id}", status_code=status.HTTP_204_NO_CONTENT)
@router.delete("/{asset_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_asset(asset_id: UUID, db: SessionDep, current_user: User = Depends(get_current_user)):
    asset = db.get(SheetAsset, asset_id)
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    sheet = db.get(Sheet, asset.sheet_id)
    workbook = db.get(Workbook, sheet.workbook_id)
    if not workbook or workbook.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Asset not found or unauthorized")
    db.delete(asset)
    db.commit()
    return None
