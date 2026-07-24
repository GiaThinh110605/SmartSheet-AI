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


def test_asset_crud(client: TestClient):
    headers = get_auth_header(client, "assetuser@example.com", "assetuser")

    wb_res = client.post("/api/v1/workbooks", json={"name": "WB For Assets"}, headers=headers)
    wb_id = wb_res.json()["id"]
    sheet_res = client.post(f"/api/v1/workbooks/{wb_id}/sheets", json={"name": "SheetAssets"}, headers=headers)
    sheet_id = sheet_res.json()["id"]

    # create asset
    payload = {"asset_type": "image", "position_config": {"x": 0, "y": 0}, "data_config": {}}
    res = client.post(f"/api/v1/sheets/{sheet_id}/assets", json=payload, headers=headers)
    assert res.status_code == 201
    asset = res.json()
    asset_id = asset["id"]

    # list assets
    res = client.get(f"/api/v1/sheets/{sheet_id}/assets", headers=headers)
    assert res.status_code == 200
    assert len(res.json()) >= 1

    # patch asset
    res = client.patch(f"/api/v1/assets/{asset_id}", json={"layer_order": 5}, headers=headers)
    assert res.status_code == 200
    assert res.json()["layer_order"] == 5

    # delete asset
    res = client.delete(f"/api/v1/assets/{asset_id}", headers=headers)
    assert res.status_code == 204
