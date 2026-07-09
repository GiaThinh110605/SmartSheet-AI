from app.core.config import settings
from sqlmodel import create_engine, Session

engine = create_engine(settings.DATABASE_URL)

db = Session(engine)
