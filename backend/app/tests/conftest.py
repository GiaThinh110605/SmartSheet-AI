from typing import Generator
from sqlmodel import SQLModel
from sqlalchemy import create_engine
from fastapi.testclient import TestClient
import pytest
from main import app
from app.db.session import get_db
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.dialects.postgresql import JSONB
from sqlmodel import Session
from app.models.user import User

DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# fixture: là dùng cho tất cả các hàm test
# name: sử dụng để các hàm test khác gọi tới
# function: làm mới hoàn toàn khi chạy hàm test kế tiếp
# Generator[a: kiểu dữ liệu trả về tại yield, b: kiểu dữ liệu send() từ bên ngoài để tương tác với nó, c: kiểu dữ liệu return khi kết thúc]
@pytest.fixture(name="session", scope="function")
def session_fixture() -> Generator[Session, None, None]:
    connection = engine.connect()
    SQLModel.metadata.create_all(connection)
    with Session(connection) as session:
        yield session
    SQLModel.metadata.drop_all(connection)
    connection.close()

@pytest.fixture(name="client")
def client_fixture(session: Session) -> Generator[TestClient, None, None]:
    def get_db_override():
        yield session
    # ghi đè db thực tế, bằng db test trong ram
    app.dependency_overrides[get_db] = get_db_override

    with TestClient(app) as client:
        yield client
    
    # reset lại dependency override sau khi test không ảnh hưởng luồng chính
    app.dependency_overrides.clear()

# chuyển đổi jsonb để test vì bảng users sử dụng jsonb
@compiles(JSONB, "sqlite")
def compile_jsonb_to_text_in_sqlite(element, compiler, **kw):
    return "TEXT"