# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# async def root():
#     return {"health": "ok!"}
from app.core.config import settings

print(settings.DATABASE_URL)