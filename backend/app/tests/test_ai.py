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


def test_ai_jobs_basic(client: TestClient):
    headers = get_auth_header(client, "aiuser@example.com", "aiuser")

    # create workbook and sheet
    wb_res = client.post("/api/v1/workbooks", json={"name": "WB AI"}, headers=headers)
    wb_id = wb_res.json()["id"]
    sheet_res = client.post(f"/api/v1/workbooks/{wb_id}/sheets", json={"name": "SheetAI"}, headers=headers)
    sheet_id = sheet_res.json()["id"]

    # create ai job
    payload = {"sheet_id": sheet_id, "job_type": "clean", "target_range": "A1:A10"}
    res = client.post("/api/v1/ai/jobs", json=payload, headers=headers)
    assert res.status_code == 201
    job = res.json()
    job_id = job["id"]

    # list jobs
    res = client.get("/api/v1/ai/jobs", headers=headers)
    assert res.status_code == 200

    # get job
    res = client.get(f"/api/v1/ai/jobs/{job_id}", headers=headers)
    assert res.status_code == 200

    # retry
    res = client.post(f"/api/v1/ai/jobs/{job_id}/retry", headers=headers)
    assert res.status_code == 200

    # cancel
    res = client.post(f"/api/v1/ai/jobs/{job_id}/cancel", headers=headers)
    assert res.status_code == 200
