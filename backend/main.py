from app.db.session import create_db_and_tables
from fastapi import FastAPI
from app.api.auth import router as auth_router
app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(auth_router, prefix="/api/v1")
