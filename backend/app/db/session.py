from typing import Annotated
from sqlmodel import SQLModel
from app.core.config import settings
from sqlmodel import create_engine, Session
from fastapi import Depends

engine = create_engine(settings.DATABASE_URL)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_db():
    with Session(engine) as db:
        yield db

SessionDep = Annotated[Session, Depends(get_db)]