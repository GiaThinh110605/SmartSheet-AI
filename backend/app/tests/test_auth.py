
from fastapi.testclient import TestClient

test_user_data = {
    "email": "testuser@example.com",
    "password": "lamgiathinhdeptrai",
    "name": "thinh lam"
}

def test_register_user_success(client: TestClient):
    response = client.post("/api/v1/auth/register", json=test_user_data)
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == test_user_data["email"]
    assert data["name"] == test_user_data["name"]
    assert "id" in data
    assert "hashed_password" not in data

def test_register_duplicate_email(client: TestClient):
    client.post("/api/v1/auth/register", json=test_user_data)
    response = client.post("/api/v1/auth/register", json=test_user_data)
    assert response.status_code == 400
    assert response.json()["detail"] == "Email already registered"

def test_login_succes(client: TestClient):
    client.post("/api/v1/auth/register", json=test_user_data)

    login_data = {
        "email": test_user_data["email"],
        "password": test_user_data["password"]
    }

    response = client.post("/api/v1/auth/login", json=login_data)
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
    assert "refresh_token" in data

def test_login_succes(client: TestClient):
    client.post("/api/v1/auth/register", json=test_user_data)

    login_data = {
        "email": test_user_data["email"],
        "password": "wrongpassword"
    }

    response = client.post("/api/v1/auth/login", json=login_data)
    assert response.status_code == 400
    assert response.json()["detail"] == "Incorrect email or password"