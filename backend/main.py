from app.db.session import create_db_and_tables
from fastapi import FastAPI
from app.api.auth import router as auth_router
from app.api.workbook import router as workbook_router
app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(auth_router, prefix="/api/v1")
app.include_router(workbook_router, prefix="/api/v1")