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


def test_column_crud(client: TestClient):
    headers = get_auth_header(client, "coluser@example.com", "coluser")

    # create workbook and sheet
    wb_res = client.post("/api/v1/workbooks", json={"name": "WB For Cols"}, headers=headers)
    wb_id = wb_res.json()["id"]
    sheet_res = client.post(f"/api/v1/workbooks/{wb_id}/sheets", json={"name": "SheetCols"}, headers=headers)
    sheet_id = sheet_res.json()["id"]

    # create column
    res = client.post(f"/api/v1/sheets/{sheet_id}/columns", json={"col_index": 1, "name": "Phone", "data_type": "text"}, headers=headers)
    assert res.status_code == 201
    col = res.json()
    col_id = col["id"]

    # list columns
    res = client.get(f"/api/v1/sheets/{sheet_id}/columns", headers=headers)
    assert res.status_code == 200
    assert len(res.json()) >= 1

    # patch column
    res = client.patch(f"/api/v1/columns/{col_id}", json={"name": "PhoneNumber"}, headers=headers)
    assert res.status_code == 200
    assert res.json()["name"] == "PhoneNumber"

    # delete column
    res = client.delete(f"/api/v1/columns/{col_id}", headers=headers)
    assert res.status_code == 204
