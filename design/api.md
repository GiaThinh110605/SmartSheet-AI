1. Authentication
Method
Endpoint
Mô tả
POST
/api/v1/auth/register
Đăng ký
POST
/api/v1/auth/token
Đăng nhập
POST
/api/v1/auth/refresh
Refresh JWT
GET
/api/v1/auth/me
Thông tin user
PATCH
/api/v1/auth/me
Cập nhật profile
DELETE
/api/v1/auth/me
Xóa tài khoản


2. Workbook APIs
CRUD
Method
Endpoint
POST
/api/v1/workbooks
GET
/api/v1/workbooks
GET
/api/v1/workbooks/{id}
PATCH
/api/v1/workbooks/{id}
DELETE
/api/v1/workbooks/{id}

Payload
{
  "name":"Sales",
  "description":"..."
}

3. Sheet APIs
CRUD
Method
Endpoint
POST
/api/v1/workbooks/{id}/sheets
GET
/api/v1/sheets/{sheet_id}
PATCH
/api/v1/sheets/{sheet_id}
DELETE
/api/v1/sheets/{sheet_id}


Load Data
GET /api/v1/sheets/{sheet_id}/data
Trả
{
    "data":[...],
    "version":5
}

Save Cells
PUT /api/v1/sheets/{sheet_id}/cells
{
  "changes":[
    {
      "row_index":1,
      "col_index":2,
      "value":"ABC"
    }
  ]
}

Batch Update
PATCH /api/v1/sheets/{sheet_id}/rows
Update nguyên hàng.

Undo
POST /api/v1/sheets/{sheet_id}/undo

Redo
POST /api/v1/sheets/{sheet_id}/redo

4. Column APIs
CRUD
Method
Endpoint
POST
/api/v1/sheets/{sheet_id}/columns
GET
/api/v1/sheets/{sheet_id}/columns
PATCH
/api/v1/columns/{column_id}
DELETE
/api/v1/columns/{column_id}

Payload
{
    "col_index":2,
    "name":"Phone",
    "data_type":"text"
}

5. Import / Export
POST /api/v1/sheets/{sheet_id}/import
multipart/form-data
file=.xlsx

GET /api/v1/sheets/{sheet_id}/export

6. Sheet Assets
Create
POST /api/v1/sheets/{sheet_id}/assets

Get
GET /api/v1/sheets/{sheet_id}/assets

Update
PATCH /api/v1/assets/{asset_id}

Delete
DELETE /api/v1/assets/{asset_id}

Payload
{
    "asset_type":"image",
    "position_config":{},
    "data_config":{}
}

7. Data Operations
Sort
POST /api/v1/sheets/{sheet_id}/sort
{
    "col_index":2,
    "order":"asc"
}

Filter
POST /api/v1/sheets/{sheet_id}/filter

Remove Duplicate
POST /api/v1/sheets/{sheet_id}/remove-duplicates

Search
POST /api/v1/sheets/{sheet_id}/search

Replace
POST /api/v1/sheets/{sheet_id}/replace

8. Chat APIs
Create Session
POST /api/v1/chat/sessions

List Session
GET /api/v1/chat/sessions

Get Session
GET /api/v1/chat/sessions/{id}

Delete Session
DELETE /api/v1/chat/sessions/{id}

Send Message
POST /api/v1/chat/messages
{
    "session_id":"",
    "role":"user",
    "content":"..."
}
voice
{
    "voice_metadata":{}
}

Get Messages
GET /api/v1/chat/sessions/{id}/messages

9. AI Chat-to-Sheet
POST /api/v1/ai/chat-to-sheet
↓
Sinh
job_id

Preview
GET /api/v1/ai/jobs/{job_id}/preview

Commit
POST /api/v1/ai/jobs/{job_id}/commit
{
    "action":"applied"
}

Cancel
POST /api/v1/ai/jobs/{job_id}/cancel

10. AI Cleaning
POST /api/v1/ai/bulk-clean
{
    "sheet_id":"",
    "col_index":3,
    "clean_type":"phone"
}

11. AI Functions
POST /api/v1/ai/custom-function
{
    "sheet_id":"",
    "function_type":"extract",
    "cells_range":"A1:A100",
    "args":[]
}

12. Natural Language Query
POST /api/v1/ai/nl-to-query
{
    "question":"..."
}

13. AI Chart
POST /api/v1/ai/nl-to-chart
{
    "prompt":"..."
}

14. OCR
Upload
POST /api/v1/ai/scan-document
multipart/form-data
file=
scan_mode=

OCR Result
GET /api/v1/uploaded-documents/{id}

Delete OCR
DELETE /api/v1/uploaded-documents/{id}

15. AI Jobs
Status
GET /api/v1/ai/jobs/{id}
↓
{
    "status":"running",
    "progress":70
}

List Jobs
GET /api/v1/ai/jobs

Retry
POST /api/v1/ai/jobs/{id}/retry

Cancel
POST /api/v1/ai/jobs/{id}/cancel

16. Audit Logs
GET /api/v1/sheets/{sheet_id}/audit-logs
Query
user_id
action_type

17. Cache
Admin
GET /api/v1/system/cache-metrics

Clear Cache
POST /api/v1/system/cache/clear

18. Health
GET /api/v1/system/health

19. WebSocket
WS /ws/chat/{session_id}
Realtime Chat

WS /ws/jobs/{job_id}
Realtime Progress

WS /ws/sheets/{sheet_id}
Realtime Collaborative Editing

