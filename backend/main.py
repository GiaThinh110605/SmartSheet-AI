from app.db.session import create_db_and_tables
from fastapi import FastAPI
from app.api.auth import router as auth_router
from app.api.workbook import router as workbook_router
from app.api.sheet import router as sheet_router
from app.api.column import router as column_router
from app.api.sheet_asset import router as sheet_asset_router
from app.api.chat import router as chat_router
from app.api.ai import router as ai_router
from app.api.uploaded_document import router as uploaded_document_router
from app.api.system import router as system_router
from app.api.ws import router as ws_router

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(auth_router, prefix="/api/v1")
app.include_router(workbook_router, prefix="/api/v1")
app.include_router(sheet_router, prefix="/api/v1")
app.include_router(column_router, prefix="/api/v1")
app.include_router(sheet_asset_router, prefix="/api/v1")
app.include_router(chat_router, prefix="/api/v1")
app.include_router(ai_router, prefix="/api/v1")
app.include_router(uploaded_document_router, prefix="/api/v1")
app.include_router(system_router, prefix="/api/v1")
app.include_router(ws_router)