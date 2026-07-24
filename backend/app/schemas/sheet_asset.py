from datetime import datetime
from typing import Dict, Optional
from uuid import UUID
from pydantic import BaseModel

class SheetAssetCreate(BaseModel):
    asset_type: str
    position_config: Optional[Dict] = None
    data_config: Optional[Dict] = None
    layer_order: Optional[int] = 0
    created_by: Optional[UUID] = None

class SheetAssetUpdate(BaseModel):
    position_config: Optional[Dict] = None
    data_config: Optional[Dict] = None
    layer_order: Optional[int] = None

class SheetAssetOut(BaseModel):
    id: UUID
    sheet_id: UUID
    asset_type: str
    position_config: Optional[Dict]
    data_config: Optional[Dict]
    layer_order: int
    created_by: Optional[UUID]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
