# 🚀 SmartSheet AI

Nền tảng bảng tính thông minh tích hợp AI tiên tiến giúp quản lý, phân tích và xử lý dữ liệu tự động.

## ✨ Tính năng chính

- **Core Spreadsheet Engine:** Bảng tính hiệu suất cao với virtual scroll
- **AI Chatbot:** Trợ lý AI hiểu ngữ cảnh bảng, hỗ trợ voice input
- **Data Auto-Processing:** Xử lý dữ liệu tự động với preview thay đổi
- **Natural Language Query:** Truy vấn dữ liệu bằng ngôn ngữ tự nhiên
- **OCR & Document Scanning:** Quét hóa đơn/chứng từ tự động
- **AI Functions:** Hàm AI tùy chỉnh như `=AI_EXTRACT()`, `=AI_CLASSIFY()`

## 🛠 Tech Stack

**Frontend:** ReactJS + Vite, Custom UI Components  
**Backend:** FastAPI (Python 3.9+), PostgreSQL, Redis  
**AI/ML:** Google Gemini 1.5 Pro, Tesseract OCR  
**DevOps:** Docker, GitHub Actions, Render/Vercel

## 📦 Cài đặt

```bash
# Clone repository
git clone https://github.com/GiaThinh110605/SmartSheet-AI.git
cd SmartSheet-AI

# Backend setup
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn main:app --reload

# Frontend setup
cd frontend
npm install
npm run dev
```

## 🚀 Deploy

**Docker Compose:**
```bash
docker-compose up -d
```

**Environment Variables:**
- `DATABASE_URL`: PostgreSQL connection string
- `REDIS_URL`: Redis connection string
- `GEMINI_API_KEY`: Google Gemini API key
- `SECRET_KEY`: JWT secret key

## 📖 Hướng dẫn sử dụng

1. **Đăng ký/Đăng nhập:** Tạo tài khoản và đăng nhập vào hệ thống
2. **Tạo Workbook:** Click "+ Bảng tính mới" từ Dashboard
3. **Sử dụng AI Chatbot:** Nhập câu lệnh hoặc dùng voice input để nhập liệu
4. **AI Functions:** Sử dụng hàm AI trong ô công thức
5. **OCR:** Quét hóa đơn/chứng từ để nhập dữ liệu tự động

## 📄 License

MIT License

## 📞 Contact

Email: lamgiathinh05@gmail.com
