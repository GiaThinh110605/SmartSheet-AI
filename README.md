# 🚀 SmartSheet AI

SmartSheet AI is a next-generation intelligent spreadsheet platform that combines traditional spreadsheet capabilities with advanced AI models. It helps users manage, analyze, and process data intuitively and automatically.

---

## 📋 Table of Contents

- [Phân tích hệ thống](#phân-tích-hệ-thống)
- [Thiết kế hệ thống](#thiết-kế-hệ-thống)
- [Hiện thực](#hiện-thực)
- [Testing](#testing)
- [Deploy](#deploy)
- [Hướng dẫn sử dụng](#hướng-dẫn-sử-dụng)

---

## 🔍 Phân tích hệ thống

SmartSheet AI là một nền tảng bảng tính thông minh thế hệ mới, tích hợp các tính năng AI tiên tiến vào quy trình làm việc với dữ liệu. Hệ thống được thiết kế để giải quyết các vấn đề thực tế trong quản lý dữ liệu doanh nghiệp:

### Vấn đề cần giải quyết
- **Nhập liệu thủ công tốn thời gian:** Nhân viên phải nhập liệu thủ công từ các nguồn khác nhau (hóa đơn, phiếu nhập kho, email...)
- **Quản lý dữ liệu phức tạp:** Các bảng tính lớn khó quản lý, dễ sai sót khi cập nhật thủ công
- **Thiếu khả năng phân tích thông minh:** Người dùng không chuyên khó khăn trong việc trích xuất thông tin từ dữ liệu
- **Quy trình số hóa tài liệu chậm:** Việc chuyển đổi tài liệu giấy sang dạng số tốn nhiều công sức

### Giải pháp SmartSheet AI
Hệ thống cung cấp 6 module chính:

1. **Core Spreadsheet Engine:** Nền tảng bảng tính hiệu suất cao với virtual scroll, hỗ trợ hàng ngàn dòng/cột
2. **Companion AI Chatbot:** Trợ lý AI đồng hành với khả năng hiểu ngữ cảnh bảng và nhập liệu bằng giọng nói
3. **Data Auto-Processing & Preview:** Xử lý dữ liệu tự động với chế độ xem trước thay đổi
4. **Natural Language Intelligence:** Truy vấn dữ liệu bằng ngôn ngữ tự nhiên và các hàm AI tùy chỉnh
5. **Image Intelligence & Document Scanning:** Quét hóa đơn/chứng từ bằng OCR và nhận diện trạng thái vật lý
6. **Backend & Compute Optimization:** Tối ưu hóa hiệu suất với caching, batching và background tasks

### Lợi ích mang lại
- **Tiết kiệm 90% thời gian nhập liệu** nhờ tự động hóa AI
- **Giảm thiểu lỗi sai sót** với chế độ xem trước và xác thực dữ liệu
- **Tăng năng suất phân tích** với truy vấn ngôn ngữ tự nhiên
- **Tối ưu chi phí** nhờ smart batching và caching thông minh

---

## 🎨 Thiết kế hệ thống

### Kiến trúc hệ thống

![Architecture Diagram](https://github.com/GiaThinh110605/SmartSheet-AI/blob/main/design/architecture.png)

Hệ thống sử dụng kiến trúc 3-tier chuẩn:

- **Frontend Layer:** ReactJS với giao diện được thiết kế trên Google Stitch
- **Backend Layer:** FastAPI với RESTful APIs và WebSocket cho real-time communication
- **Data Layer:** PostgreSQL cho dữ liệu chính, Redis cho caching và message queue

### Thiết kế cơ sở dữ liệu

![Database Design](https://github.com/GiaThinh110605/SmartSheet-AI/blob/main/design/designDatabase.png)

Cơ sở dữ liệu được thiết kế theo mô hình relational với các bảng chính:
- `users` - Quản lý người dùng
- `workbooks` - Quản lý workbook/sách làm việc
- `sheets` - Quản lý các sheet trong workbook
- `columns` - Định nghĩa cấu trúc cột
- `cells` - Lưu trữ dữ liệu từng ô
- `chat_sessions` - Quản lý phiên chat
- `chat_messages` - Lưu trữ tin nhắn
- `ai_jobs` - Theo dõi các tác vụ AI
- `audit_logs` - Nhật ký hoạt động

### Thiết kế giao diện UI/UX

[SmartSheet AI UI Design on Google Stitch](https://stitch.withgoogle.com/projects/6547954069371395139)

Giao diện được thiết kế theo phong cách B2B SaaS hiện đại với:
- **Color Palette:** Deep Blue (#1E3A8A) làm màu chính, Cyan (#06B6D4) làm màu nhấn
- **Typography:** Font Inter cho readability cao
- **Layout:** 3-column layout cho editor (Sidebar 18% - Grid 57% - AI Chat 25%)
- **Components:** Modal, Card, Button, Input với consistent design tokens

### API Architecture

Hệ thống cung cấp 19 nhóm API chính:
1. Authentication - Đăng ký, đăng nhập, refresh token
2. Workbook APIs - CRUD workbook
3. Sheet APIs - Quản lý sheet, load/save data, undo/redo
4. Column APIs - Định nghĩa cấu trúc cột
5. Import/Export - Xử lý file .xlsx, .csv
6. Sheet Assets - Quản lý hình ảnh, shapes
7. Data Operations - Sort, filter, search, replace
8. Chat APIs - Quản lý chat session và messages
9. AI Chat-to-Sheet - Nhập liệu từ chat
10. AI Cleaning - Làm sạch dữ liệu hàng loạt
11. AI Functions - Hàm AI tùy chỉnh
12. Natural Language Query - Truy vấn bằng ngôn ngữ tự nhiên
13. AI Chart - Tạo biểu đồ tự động
14. OCR - Quét tài liệu
15. AI Jobs - Quản lý tác vụ AI
16. Audit Logs - Nhật ký hoạt động
17. Cache - Quản lý cache
18. Health - Health check
19. WebSocket - Real-time communication

---

## 💻 Hiện thực

### Tech Stack

#### Frontend
- **Framework:** ReactJS với Vite
- **UI Library:** Custom components với design system từ Stitch
- **State Management:** React Context + Hooks
- **HTTP Client:** Axios
- **WebSocket:** Native WebSocket API
- **Build Tool:** Vite

#### Backend
- **Framework:** FastAPI (Python 3.9+)
- **Database:** PostgreSQL 14+
- **Cache:** Redis 7+
- **Task Queue:** Celery + Redis
- **Authentication:** JWT (OAuth2 with Password)
- **API Documentation:** Swagger/OpenAPI

#### AI/ML
- **LLM:** Google Gemini 1.5 Pro
- **OCR:** Tesseract + Custom Vision Model
- **Voice-to-Text:** Web Speech API (Browser native)
- **NLP:** Custom prompt engineering với Gemini

#### DevOps
- **Containerization:** Docker & Docker Compose
- **CI/CD:** GitHub Actions
- **Deployment:** Render (Backend), Vercel (Frontend)
- **Monitoring:** Custom health endpoints

### Cấu trúc dự án

```
SmartSheet-AI/
├── backend/
│   ├── app/
│   │   ├── api/          # API endpoints
│   │   ├── core/         # Config, security, dependencies
│   │   ├── db/           # Database connection
│   │   ├── models/       # SQLAlchemy models
│   │   ├── schemas/      # Pydantic schemas
│   │   ├── services/     # Business logic
│   │   ├── utils/        # Utilities
│   │   └── workers/      # Celery workers
│   ├── main.py           # Application entry point
│   └── requirements.txt  # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── components/   # React components
│   │   ├── pages/        # Page components
│   │   ├── services/     # API services
│   │   ├── hooks/        # Custom hooks
│   │   └── utils/        # Utilities
│   └── package.json      # Node dependencies
├── design/
│   ├── architecture.png # System architecture diagram
│   ├── designDatabase.png # Database schema
│   ├── api.md           # API documentation
│   └── designUI.md      # UI/UX specifications
└── README.md
```

### Các module chính

#### 1. Core Spreadsheet Engine
- Sử dụng FortuneSheet/Luckysheet cho grid rendering
- Virtual scroll để tối ưu performance với large datasets
- Cell coordinate mapping với row_index, col_index
- Dynamic column definition với data type enforcement

#### 2. Companion AI Chatbot
- WebSocket connection cho real-time chat
- Context-aware: Tự động đọc cấu trúc sheet hiện tại
- Voice-to-text với Web Speech API
- Session memory để duy trì ngữ cảnh hội thoại

#### 3. Data Auto-Processing & Preview
- Chat-to-Sheet: Parse natural language thành structured data
- Visual Diff Preview: Hiển thị thay đổi với màu đỏ/xanh
- Human-in-the-loop: Nút Apply/Cancel để xác nhận
- Bulk Data Cleaning: Chuẩn hóa dữ liệu hàng loạt

#### 4. Natural Language Intelligence
- Custom AI Functions: `=AI_EXTRACT()`, `=AI_CLASSIFY()`
- Natural Language to Query: Dịch câu hỏi thành filter logic
- Auto Chart Generation: Tự động chọn loại biểu đồ phù hợp

#### 5. Image Intelligence
- OCR với Tesseract + Vision Model
- Layout analysis cho invoices/receipts
- Physical state recognition cho inventory counting

#### 6. Backend Optimization
- Smart Request Batching: Gộp requests để tiết kiệm API calls
- Response Caching: Redis cache cho computed values
- Background Tasks: Celery cho heavy operations

---

## 🧪 Testing

### Backend Testing (Pytest)

```bash
cd backend
pytest tests/ -v
```

**Test coverage bao gồm:**
- Unit tests cho các service functions
- Integration tests cho API endpoints
- Database operation tests
- AI function tests với mocked responses

### Frontend Testing

```bash
cd frontend
npm test
```

**Test coverage bao gồm:**
- Component unit tests
- Integration tests cho user flows
- API service tests

### Manual Testing Checklist

1. **Authentication Flow**
   - [ ] Đăng ký tài khoản mới
   - [ ] Đăng nhập với credentials đúng
   - [ ] Refresh token hoạt động
   - [ ] Logout thành công

2. **Spreadsheet Operations**
   - [ ] Tạo workbook mới
   - [ ] Thêm/sửa/xóa sheet
   - [ ] Nhập/sửa/xóa cell data
   - [ ] Sort/filter data
   - [ ] Import file Excel
   - [ ] Export file Excel

3. **AI Chatbot**
   - [ ] Gửi tin nhắn text
   - [ ] Voice input hoạt động
   - [ ] Context-aware responses
   - [ ] Chat-to-Sheet functionality
   - [ ] Apply/Cancel changes

4. **AI Functions**
   - [ ] `=AI_EXTRACT()` hoạt động
   - [ ] `=AI_CLASSIFY()` hoạt động
   - [ ] Natural language query
   - [ ] Auto chart generation

5. **OCR/Document Scanning**
   - [ ] Upload ảnh hóa đơn
   - [ ] OCR accuracy > 90%
   - [ ] Data extraction chính xác
   - [ ] Import vào sheet thành công

---

## 🚀 Deploy

### Prerequisites

- Docker & Docker Compose
- PostgreSQL 14+
- Redis 7+
- Python 3.9+
- Node.js 18+
- Google Gemini API Key

### Local Development Setup

#### 1. Clone repository
```bash
git clone https://github.com/GiaThinh110605/SmartSheet-AI.git
cd SmartSheet-AI
```

#### 2. Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your configuration
uvicorn main:app --reload
```

#### 3. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

#### 4. Database Migration
```bash
cd backend
alembic upgrade head
```

### Production Deployment

#### Using Docker Compose

```bash
docker-compose up -d
```

#### Deploy to Render (Backend)

1. Connect GitHub repository to Render
2. Create Web Service with:
   - Build Command: `cd backend && pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
3. Add environment variables from `.env`
4. Deploy

#### Deploy to Vercel (Frontend)

1. Connect GitHub repository to Vercel
2. Configure build settings:
   - Framework: Vite
   - Build Command: `cd frontend && npm run build`
   - Output Directory: `frontend/dist`
3. Add environment variables for API URL
4. Deploy

### Environment Variables

**Backend (.env):**
```env
DATABASE_URL=postgresql://user:password@localhost:5432/smartsheet
REDIS_URL=redis://localhost:6379/0
SECRET_KEY=your-secret-key
GEMINI_API_KEY=your-gemini-api-key
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

**Frontend (.env):**
```env
VITE_API_URL=https://your-backend-api.com
VITE_WS_URL=wss://your-backend-api.com
```

---

## 📖 Hướng dẫn sử dụng

### Đăng ký và Đăng nhập

1. Truy cập [SmartSheet AI](https://your-app.com)
2. Click "Đăng ký" để tạo tài khoản mới
3. Nhập email, mật khẩu và thông tin cá nhân
4. Xác nhận email (nếu có bật)
5. Đăng nhập với credentials đã tạo

### Tạo Workbook mới

1. Từ Dashboard, click "+ Bảng tính mới"
2. Chọn template từ danh sách:
   - Tờ trắng
   - Bảng lương
   - Quản lý kho
   - Hóa đơn nhập
   - Báo cáo doanh thu
   - Kiểm kê tài sản
3. Nhập tên và mô tả cho workbook
4. Click "Tạo bảng tính"

### Sử dụng Spreadsheet Editor

**Cấu trúc giao diện:**
- **Left Sidebar:** Danh sách workbook và sheets
- **Central Grid:** Khu vực làm việc chính với bảng tính
- **Right Sidebar:** Trợ lý AI Chatbot

**Thao tác cơ bản:**
- **Nhập liệu:** Click vào ô và gõ dữ liệu
- **Sửa cell:** Double-click vào ô để sửa
- **Định dạng cột:** Click header để đặt tên và kiểu dữ liệu
- **Sort/Filter:** Sử dụng toolbar ở trên grid
- **Import file:** Click "Nhập file Excel" để upload .xlsx/.csv
- **Export file:** Click "Export" để tải về file Excel

### Sử dụng AI Chatbot

**Chat cơ bản:**
1. Nhập câu hỏi hoặc lệnh vào ô chat
2. Click nút gửi hoặc nhấn Enter
3. AI sẽ phản hồi dựa trên ngữ cảnh sheet hiện tại

**Voice Input:**
1. Click nút micro ở ô chat
2. Nói câu lệnh của bạn
3. AI sẽ chuyển đổi thành text và xử lý

**Chat-to-Sheet (Nhập liệu từ chat):**
```
User: "Anh Nam mua 3 cái ghế chưa trả tiền"
AI: Sẽ tự động điền vào các cột: Khách hàng, Số lượng, Sản phẩm, Trạng thái
```

**Xem trước và áp dụng thay đổi:**
1. AI sẽ hiển thị preview với màu xanh (giá trị mới) và đỏ (giá trị cũ)
2. Review các thay đổi
3. Click "Áp dụng" để xác nhận hoặc "Hủy" để bỏ qua

### Sử dụng AI Functions

**=AI_EXTRACT(cell, "yêu cầu"):**
```
=AI_EXTRACT(A2, "Mã đơn hàng")
Trích xuất mã đơn hàng từ chuỗi text trong ô A2
```

**=AI_CLASSIFY(cell, "danh sách nhãn"):**
```
=AI_CLASSIFY(B2, "Tích cực,Tiêu cực,Trung lập")
Phân loại nội dung trong ô B2 thành các nhãn
```

### Natural Language Query

**Ví dụ truy vấn:**
- "Ai là người mua nhiều hàng nhất trong tháng 5?"
- "Tổng doanh thu quý 2 là bao nhiêu?"
- "Liệt kê các sản phẩm tồn kho dưới 10 cái"

AI sẽ tự động:
1. Phân tích câu hỏi
2. Dịch thành logic lọc
3. Ẩn các dòng không liên quan
4. Highlight kết quả

### Quét hóa đơn/chứng từ (OCR)

1. Click "Quét hóa đơn" từ quick actions
2. Kéo thả ảnh hóa đơn vào vùng upload
3. Chọn loại tài liệu (Hóa đơn GTGT, Phiếu nhập kho, Biên lai...)
4. AI sẽ tự động:
   - Phân tích layout tài liệu
   - Trích xuất dữ liệu sản phẩm
   - Nhận diện số lượng, đơn giá, thành tiền
5. Review kết quả trong preview table
6. Chọn sheet đích và click "Nhập vào bảng tính"

### Cài đặt và Tùy chỉnh

**Truy cập Settings:**
1. Click avatar ở top-right
2. Chọn "Cài đặt"

**Các tùy chỉnh:**
- **Tài khoản:** Cập nhật thông tin cá nhân
- **Cài đặt AI:** Chọn model AI, bật/tắt xác nhận trước khi áp dụng
- **Giao diện:** Tùy chỉnh theme, ngôn ngữ
- **Lịch sử hoạt động:** Xem audit logs

### Keyboard Shortcuts

- `Ctrl/Cmd + S`: Save workbook
- `Ctrl/Cmd + Z`: Undo
- `Ctrl/Cmd + Y`: Redo
- `Ctrl/Cmd + F`: Search trong sheet
- `Ctrl/Cmd + B`: Bold text
- `Ctrl/Cmd + I`: Italic text

### Troubleshooting

**AI không phản hồi:**
- Kiểm tra kết nối internet
- Xác nhận API key còn hợp lệ
- Kiểm tra quota AI usage

**Không thể import file:**
- Đảm bảo file là .xlsx hoặc .csv
- Kiểm tra kích thước file < 10MB
- Thử lại với file khác

**OCR không chính xác:**
- Đảm bảo ảnh rõ nét, đủ sáng
- Sử dụng ảnh thẳng đứng, không bị méo
- Thử với định dạng tài liệu khác

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 📞 Contact

For support, please contact [lamgiathinh05@gmail.com] or open an issue on GitHub.
