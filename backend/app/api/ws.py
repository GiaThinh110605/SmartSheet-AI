from fastapi import APIRouter, WebSocket, WebSocketDisconnect

router = APIRouter()

@router.websocket("/ws/chat/{session_id}")
async def ws_chat(session_id: str, websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"echo chat {session_id}: {data}")
    except WebSocketDisconnect:
        return

@router.websocket("/ws/jobs/{job_id}")
async def ws_jobs(job_id: str, websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"echo job {job_id}: {data}")
    except WebSocketDisconnect:
        return

@router.websocket("/ws/sheets/{sheet_id}")
async def ws_sheets(sheet_id: str, websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"echo sheet {sheet_id}: {data}")
    except WebSocketDisconnect:
        return
