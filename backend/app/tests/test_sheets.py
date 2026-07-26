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


def test_sheet_crud(client: TestClient):
    headers = get_auth_header(client, "sheetuser@example.com", "sheetuser")

    # create workbook
    wb_res = client.post("/api/v1/workbooks", json={"name": "WB For Sheets"}, headers=headers)
    assert wb_res.status_code == 201
    wb = wb_res.json()
    wb_id = wb["id"]

    # create sheet
    res = client.post(f"/api/v1/workbooks/{wb_id}/sheets", json={"name": "Sheet1"}, headers=headers)
    assert res.status_code == 201
    sheet = res.json()
    sheet_id = sheet["id"]

    # get sheet
    res = client.get(f"/api/v1/sheets/{sheet_id}", headers=headers)
    assert res.status_code == 200

    # get data
    res = client.get(f"/api/v1/sheets/{sheet_id}/data", headers=headers)
    assert res.status_code == 200

    # save cell
    res = client.put(f"/api/v1/sheets/{sheet_id}/cells", json=[{"row_index": 0, "col_index": 0, "value": "A1"}], headers=headers)
    assert res.status_code == 200
    data = res.json()
    assert data[0]["value"] == "A1"

    # batch update rows
    res = client.patch(f"/api/v1/sheets/{sheet_id}/rows", json={"rows": [{"row_index": 0, "values": {"0": "A1"}}]}, headers=headers)
    assert res.status_code == 200

    # delete sheet
    res = client.delete(f"/api/v1/sheets/{sheet_id}", headers=headers)
    assert res.status_code == 204
