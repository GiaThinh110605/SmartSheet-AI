# 🚀 SmartSheet AI

SmartSheet AI is a next-generation intelligent spreadsheet platform that combines traditional spreadsheet capabilities with advanced AI models. It helps users manage, analyze, and process data intuitively and automatically.

## 🌟 Core Features

- **Spreadsheet Engine:** High-performance grid rendering (virtual scroll), dynamic column structures, import/export (.xlsx, .csv), and basic sheet operations (sorting, drawing, shapes).
- **Companion AI Chatbot:** Context-aware real-time chat with voice-to-text support and session memory for conversational data manipulation.
- **Auto-Processing & Preview:** "Chat-to-Sheet" for natural language data entry, visual diff previews for AI suggestions, human-in-the-loop validation, and bulk data cleaning.
- **Natural Language Intelligence:** Custom AI formulas (`=AI_EXTRACT`, `=AI_CLASSIFY`), natural language to data query, and automatic chart generation.
- **Image Intelligence:** "Scan-to-Sheet" for invoices and receipts using OCR, and physical state recognition (e.g., counting inventory via images).
- **MLOps & Backend Optimization:** Smart request batching, <50ms response caching (Redis/Postgres), and asynchronous background task queues for heavy operations.

---

## 🛠 Tech Stack

### Frontend
- **Framework:** ReactJS
- **Design UI/UX:** Stitch

### Backend & Database
- **Framework:** FastAPI
- **Database:** PostgreSQL
- **Design Database:** Use Case Diagram

### CI/CD & Deploy
- **Workflow:** GitHub Actions
- **Containerization:** Docker
- **Deploy:** Render, Vercel

### Unit Testing
- **Framework:** Pytest

### AI & Tools
- **AI Features:** Voice to text, Chatbot, Document OCR, NLP Querying
- **Assistant Tool:** Antigravity, Codex
