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


def test_chat_session_and_messages(client: TestClient):
    headers = get_auth_header(client, "chatuser@example.com", "chatuser")

    # create workbook and sheet
    wb_res = client.post("/api/v1/workbooks", json={"name": "WB Chat"}, headers=headers)
    wb_id = wb_res.json()["id"]
    sheet_res = client.post(f"/api/v1/workbooks/{wb_id}/sheets", json={"name": "SheetChat"}, headers=headers)
    sheet_id = sheet_res.json()["id"]

    # create chat session
    res = client.post("/api/v1/chat/sessions", json={"sheet_id": sheet_id, "title": "Session1"}, headers=headers)
    assert res.status_code == 201
    session = res.json()
    session_id = session["id"]

    # send message
    msg_payload = {"session_id": session_id, "role": "user", "content": "hello"}
    res = client.post(f"/api/v1/chat/sessions/{session_id}/messages", json=msg_payload, headers=headers)
    assert res.status_code == 201

    # get messages
    res = client.get(f"/api/v1/chat/sessions/{session_id}/messages", headers=headers)
    assert res.status_code == 200
    assert len(res.json()) >= 1
