
from fastapi.testclient import TestClient

def get_auth_header(client: TestClient, email: str, name: str):
    client.post("/api/v1/auth/register", json={
        "email": email,
        "password": "password123",
        "name": name
    })
    login_res = client.post("/api/v1/auth/login", json={
        "email": email,
        "password": "password123"
    })
    token = login_res.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}

def test_create_workbook_success(client: TestClient):
    headers = get_auth_header(client, "user@gmail.com", "test")
    payload = {
        "name": "Sales",
        "description": "Sales workbook",
        "meta_data": {"tags": ["sales", "Q3"]}
    }

    response = client.post("/api/v1/workbooks", headers=headers, json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Sales"
    assert data["description"] == "Sales workbook"
    assert data["meta_data"] == {"tags": ["sales", "Q3"]}
    assert "id" in data
    assert "created_at" in data
    assert "updated_at" in data

def test_get_workbook_list(client: TestClient):
    headers = get_auth_header(client, "user1@gmail.com", "test1")

    client.post("/api/v1/workbooks", json={"name": "Book A"}, headers=headers)
    client.post("/api/v1/workbooks", json={"name": "Book B"}, headers=headers)
    
    response = client.get("/api/v1/workbooks", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["name"] == "Book A"
    assert data[1]["name"] == "Book B"
    assert "id" in data[0]
    assert "id" in data[1]

def test_patch_workbook(client: TestClient):
    headers = get_auth_header(client, "user2@gmail.com", "test2")

    create_res = client.post("/api/v1/workbooks", json={"name": "Book C"}, headers=headers)
    workbook = create_res.json()["id"]

    update_payload = {
        'name': "thinh",
        "description": "kkk"
    }
    response = client.patch(f"/api/v1/workbooks/{workbook}", json=update_payload, headers=headers)
    assert response.status_code == 200
    assert response.json()["name"] == "thinh"
    assert response.json()["description"] == "kkk"
    
def test_delete_workbook(client: TestClient):
    headers = get_auth_header(client, "user3@gmail.com", "test3")
    
    create_res = client.post("/api/v1/workbooks", json={"name": "Book C"}, headers=headers)
    workbook = create_res.json()["id"]

    response = client.delete(f"/api/v1/workbooks/{workbook}", headers=headers)
    assert response.status_code == 204
    