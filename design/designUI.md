# SmartSheet AI — Stitch UI Design Prompt

## Application Overview
Design a **complete, production-ready web application UI** called **"SmartSheet AI"** — a high-end AI-powered spreadsheet SaaS platform (combination of Excel + AI Chatbot + Document OCR Scanner). The interface must feel like a premium B2B SaaS tool: clean, minimal, trustworthy, and futuristic. Use **Vietnamese language** throughout the interface.
All screens must use exactly the same design system, color palette, typography, spacing, border-radius, shadows, and component styles.

---

## Design System (Apply to ALL Screens)

### Color Palette
| Role | Name | Hex |
|---|---|---|
| Primary Dark | Deep Blue | `#1E3A8A` |
| Primary Light | Cyan | `#06B6D4` |
| Accent Success | Emerald Green | `#10B981` |
| Accent Warning | Amber | `#F59E0B` |
| Accent Danger | Red | `#EF4444` |
| Background | White | `#FFFFFF` |
| Surface | Light Gray | `#F8FAFC` |
| Border | Slate | `#E2E8F0` |
| Text Primary | Dark Slate | `#0F172A` |
| Text Secondary | Slate Gray | `#64748B` |
| Text Muted | Light Slate | `#94A3B8` |
| Sidebar BG | Deep Blue | `#1E3A8A` |
| Sidebar Text | White | `#FFFFFF` |
| Sidebar Active | Cyan | `#06B6D4` |
| AI Pending Cell BG | Green Tint | `#D1FAE5` |
| AI Old Cell BG | Red Tint | `#FEE2E2` |
| Status Running | Cyan | `#06B6D4` |
| Status Done | Green | `#10B981` |
| Status Pending | Amber | `#F59E0B` |
| Status Failed | Red | `#EF4444` |

### Typography
- **Font**: Inter (Google Fonts)
- **Heading**: Inter 700, `#0F172A`
- **Body**: Inter 400, `#0F172A`
- **Caption/Muted**: Inter 400, `#64748B`
- **Code/Cell**: Inter Mono 400

### Spacing & Radius
- Base unit: 4px
- Card border-radius: 12px
- Button border-radius: 8px
- Input border-radius: 8px
- Modal border-radius: 16px
- Sidebar width (left): 18% of viewport
- Sidebar width (right / AI): 25% of viewport

### Shadows
- Card: `0 1px 3px rgba(0,0,0,0.08), 0 1px 2px rgba(0,0,0,0.04)`
- Modal: `0 20px 60px rgba(0,0,0,0.15)`
- Dropdown: `0 4px 16px rgba(0,0,0,0.10)`

---

## Screen 1: Dashboard / Home Screen
**Route:** `/dashboard` | **Full page, light background `#F8FAFC`**

### Top Navigation Bar (height: 64px, bg: `#FFFFFF`, border-bottom: `#E2E8F0`)
- Left: Logo "SmartSheet AI" — the letters "Smart" in `#1E3A8A` bold, "Sheet AI" in `#06B6D4` bold — with a small grid+sparkle icon in cyan
- Center: Search bar (placeholder: "Tìm kiếm bảng tính...", width: 40%, rounded, icon left)
- Right: Bell icon (notification), Avatar circle (user photo + name "Nguyễn Văn A"), button "+ Bảng tính mới" (bg: `#1E3A8A`, text white, rounded-lg)

### Page Layout (two columns: left 70%, right 30%)

**Left Column:**

#### Stats Row (4 stat cards in a horizontal row)
Each stat card: white bg, border `#E2E8F0`, border-radius 12px, padding 20px
- Card 1: Icon grid (cyan), label "Tổng bảng tính", value "24", sub "↑ 3 tuần này"
- Card 2: Icon AI sparkle (blue), label "AI đã dùng tháng này", value "1,240 / 2,000", sub-progress bar (62% filled, color `#06B6D4`)
- Card 3: Icon file (green), label "Tài liệu đã quét", value "87"
- Card 4: Icon clock (amber), label "Lần đồng bộ cuối", value "2 phút trước"

#### Workbook Cards Grid (3 columns, gap 16px)
Each workbook card (bg: white, border: `#E2E8F0`, radius 12px, shadow):
- Top: Thumbnail preview area (height 120px, bg gradient from `#EFF6FF` to `#DBEAFE`) showing mini grid lines
- Body: Workbook name bold `#0F172A`, description in `#64748B` small
- Footer: "Chỉnh sửa lần cuối: 2 giờ trước" + small avatar of owner + kebab menu icon
- Show 6 cards: "Bảng lương tháng 7", "Báo cáo kho bãi Q2", "Hóa đơn nhập hàng", "Doanh thu 2025", "Kiểm kê sản phẩm", "Chi phí vận hành"

**Right Column:**

#### Recent Activity Feed (card: white bg, border, radius 12px, padding 20px)
Title: "Hoạt động gần đây" bold
Each activity item (border-bottom `#F1F5F9`, padding 12px 0):
- Small colored dot + action text + time ago
- Items: "AI đã cập nhật 15 dòng trong Bảng lương · 5 phút" (green dot), "Quét hóa đơn hoàn tất · 12 phút" (cyan dot), "Nguyễn Văn B đã chỉnh sửa Báo cáo kho · 1 giờ" (blue dot), "Xuất file Excel thành công · 3 giờ" (gray dot)

#### Quick Actions (4 buttons in 2x2 grid, inside a card)
Title: "Thao tác nhanh"
- "📄 Tạo bảng mới" (bg `#EFF6FF`, text `#1E3A8A`)
- "📷 Quét hóa đơn" (bg `#ECFDF5`, text `#10B981`)
- "📥 Nhập file Excel" (bg `#FFFBEB`, text `#F59E0B`)
- "🤖 Hỏi trợ lý AI" (bg `#EFF6FF`, text `#06B6D4`)

---

## Screen 2: Main Spreadsheet Editor
**Route:** `/workbook/:id/sheet/:id` | **Full page, 3-column layout**

### Top Navigation Bar (height: 56px, bg: `#FFFFFF`, border-bottom: `#E2E8F0`)
- Logo (small, left)
- Workbook name: editable inline input "Bảng lương tháng 7" — clicking makes it an editable text field
- Sheet tabs (horizontal): "Sheet 1 | Nhân viên | Lương cơ bản +" — active tab has bottom border `#06B6D4`, text `#1E3A8A`
- Right: "💾 Đã lưu" green text + timestamp, share icon, export button

### Toolbar (height: 44px, bg: `#F8FAFC`, border-bottom: `#E2E8F0`)
Groups of icon buttons: Bold, Italic, Underline | Align left/center/right | Font size | Text color | Background color | Merge cells | Borders | Number format | Sort ↑↓ | Filter | Insert (image/chart/shape) | AI Functions dropdown

### Main Layout (three columns)

**Left Sidebar (18% width, bg: `#1E3A8A`, text: white)**
- Section "BỘ SƯU TẬP" with collapse arrow
  - Folder icon + "Bảng lương 2025" (bold, active, text cyan `#06B6D4`)
  - Folder icon + "Kho bãi Q2"
  - Folder icon + "Hóa đơn 2025"
  - "+ Thêm workbook" (muted, dashed border)
- Section "SHEETS" below
  - Sheet icon + "Nhân viên" (active, bg `rgba(6,182,212,0.15)`, left border 3px `#06B6D4`)
  - Sheet icon + "Lương cơ bản"
  - Sheet icon + "Phụ cấp"
  - "+ Thêm sheet" muted

**Central Grid Area (57% width, bg: `#FFFFFF`)**
- Column headers row (bg: `#F1F5F9`, height 32px):
  - Row number column (40px wide, bg `#F8FAFC`)
  - Column A: "Họ và Tên" with text icon "T" in `#64748B` — sort arrow on hover
  - Column B: "Mã nhân viên" with text icon "T"
  - Column C: "Ngày vào làm" with calendar icon in `#06B6D4`
  - Column D: "Lương cơ bản" with hash "#" icon in `#10B981`
  - Column E: "Trạng thái" with tag icon
  - Column F onwards: more columns...
- Grid rows (alternate bg: white and `#FAFAFA`, height 36px per row):
  - Row 1: "Nguyễn Văn An | NV001 | 15/03/2022 | 12,000,000 | Đang làm việc"
  - Row 2: "Trần Thị Bình | NV002 | 01/07/2021 | 15,500,000 | Đang làm việc"
  - Row 3 (PENDING STATE — AI suggested): cells bg `#D1FAE5`, text `#10B981` — showing AI is proposing new values
  - Row 4: "Lê Minh Cường | NV004 | 22/11/2023 | 9,800,000 | Đang làm việc"
  - Row 5 (OLD VALUE — being replaced): cell bg `#FEE2E2`, text `#EF4444` with strikethrough on old value
  - Rows continue to fill the screen...
- Cell selection: selected cell has border `2px solid #06B6D4`
- Formula/address bar above grid: "A3" cell reference box + "=" formula bar

**Right Sidebar — AI Companion (25% width, bg: `#FFFFFF`, border-left: `#E2E8F0`)**
- Header (bg: `#1E3A8A`, padding 16px, radius top):
  - Left: Cyan sparkle AI avatar circle + "Trợ lý AI" white bold + "SmartSheet AI" white small
  - Right: Minimize icon (white)
- Chat Message History (scrollable, padding 12px, gap 12px):
  - User bubble (bg: `#EFF6FF`, border `#BFDBFE`, align right, radius 12px 12px 0 12px): "Chuẩn hóa toàn bộ số điện thoại trong cột E về định dạng 0xxxxxxxxx"
  - AI bubble (bg: `#F8FAFC`, border `#E2E8F0`, align left, radius 0 12px 12px 12px): "Tôi sẽ kiểm tra và chuẩn hóa 156 số điện thoại trong cột E. Xem trước thay đổi:"
  - AI preview chip (bg `#D1FAE5`, border `#6EE7B7`): "✨ 23 ô sẽ được cập nhật · Xem trước"
  - User bubble: "Áp dụng đi"
  - AI bubble: "Đã áp dụng thành công! Tất cả số điện thoại đã được chuẩn hóa."
- Chat Input Area (border-top `#E2E8F0`, padding 12px):
  - Text input (placeholder: "Hỏi trợ lý AI hoặc ra lệnh...", full width, rounded)
  - Right of input: Microphone button (round, bg `#1E3A8A`, white mic icon) — with "pulse" animation ring in cyan when active
  - Send button (bg `#06B6D4`)
- Action Buttons (padding 12px, two buttons full-width):
  - "✓ Áp dụng" (bg: `#10B981`, text white, rounded-lg, height 44px, full width, bold)
  - "✕ Hủy bỏ" (bg: `#F1F5F9`, text `#64748B`, rounded-lg, height 44px, full width)

### Bottom Status Bar (height: 32px, bg: `#F8FAFC`, border-top: `#E2E8F0`)
- Left: "Tổng: 156 dòng · 8 cột"
- Center: "Chế độ xem trước AI đang bật — 23 thay đổi chờ xác nhận" in amber `#F59E0B`
- Right: "AI: 1,240 / 2,000 lượt · Đồng bộ lần cuối: 2 phút trước" in `#64748B`

---

## Screen 3: Document Upload & Scan Screen
**Route:** `/scan` | **Modal overlay on top of editor, semi-transparent bg `rgba(15,23,42,0.6)`**

### Modal (bg: white, radius: 20px, shadow: heavy, width: 85vw, height: 85vh)

**Modal Header** (border-bottom `#E2E8F0`, padding 24px):
- Left: "📷 Quét & Nhập tài liệu" bold `#0F172A` 20px
- Right: X close button

**Modal Body (two columns: left 45%, right 55%)**

**Left — Upload Zone:**
- Large drag-and-drop area (height: 300px, border: 2px dashed `#06B6D4`, bg: `#F0FFFE`, radius 16px, centered content):
  - Big upload icon (cyan `#06B6D4`, 48px)
  - "Kéo thả ảnh hoặc PDF vào đây" bold `#0F172A`
  - "Hỗ trợ: JPG, PNG, PDF · Tối đa 10MB" small `#64748B`
  - "hoặc" divider
  - "Chọn file từ máy tính" button (outlined, `#1E3A8A`)
- File type chips below: [📄 Hóa đơn GTGT] [📦 Phiếu nhập kho] [🧾 Biên lai] [📊 Bảng tính]
- Uploaded file preview (if file selected): file thumbnail + name + size + remove button

**Right — OCR Live Preview:**
- Sub-header: "Kết quả nhận dạng" + status badge "Đang xử lý..." (amber, pulsing dot)
- AI processing progress bar (bg `#DBEAFE`, fill `#06B6D4`, height 6px, animated) — "Đang phân tích cấu trúc tài liệu... 67%"
- Mini spreadsheet preview table (showing extracted data):
  - Header row (bg `#1E3A8A`, text white): "Tên hàng | Số lượng | Đơn giá | Thành tiền"
  - Rows being populated with animation: "Ghế văn phòng | 10 | 850,000 | 8,500,000" etc.
  - Newly detected cells animate in with a flash of `#D1FAE5`
- OCR confidence score: "Độ chính xác: 94%" with green badge
- Destination: "Nhập vào sheet:" dropdown — "Hóa đơn nhập hàng → Sheet 2"

**Modal Footer** (border-top, padding 20px, flex end):
- "Hủy" gray outlined button
- "Nhập vào bảng tính →" (bg `#10B981`, white, bold, rounded-lg)

---

## Screen 4: AI Diff Preview Modal
**Route:** Modal overlay | `rgba(15,23,42,0.7)` backdrop**

### Modal (bg: white, radius: 20px, width: 90vw, max-height: 80vh)

**Modal Header** (bg: `#1E3A8A`, rounded top, padding 20px 24px):
- Left: Cyan sparkle icon + "Xem trước thay đổi AI" white bold 18px
- Sub: "23 ô sẽ được cập nhật trong cột E (E2:E156)" white muted small
- Right: X close (white)

**Modal Body — Side-by-side diff view (two equal columns, gap 1px bg `#E2E8F0`)**

**Left column header** (bg `#FEE2E2`, text `#EF4444` bold, padding 12px 16px): "← Dữ liệu hiện tại"
**Right column header** (bg `#D1FAE5`, text `#10B981` bold, padding 12px 16px): "→ AI đề xuất"

**Diff rows (alternating light bg, each row split left/right)**:
Each diff row shows: Row number (gray pill) | Left cell value (if changed: red bg `#FEE2E2`, strikethrough text `#EF4444`) | Right cell value (green bg `#D1FAE5`, text `#10B981` bold)
- Row 3: "0912345678" (red strikethrough) | "0912.345.678" (green) — example phone format
- Row 7: "912345678" (red, missing leading 0) | "0912345678" (green)
- Row 12: unchanged rows show identical values, bg white, no color
- Show 8-10 rows, with scroll indicator

**Modal Footer** (border-top, padding 20px 24px, space-between):
- Left: "23 thay đổi · 0 lỗi" badge in green
- Right: "Hủy toàn bộ" (outlined, `#EF4444` text) + "✓ Áp dụng tất cả" (bg `#10B981`, white, bold, rounded-lg, large)

---

## Screen 5: AI Job Status Panel
**Design:** Floating panel (bottom-right corner, width 380px, shadow heavy) OR full overlay when multiple jobs**

**Panel Header** (bg: `#1E3A8A`, radius top 16px, padding 16px 20px):
- "⚡ AI đang xử lý" white bold + live pulsing green dot
- X minimize button (white)

**Job List (scrollable, bg white, padding 12px, gap 8px)**:

Each job card (bg: `#F8FAFC`, border `#E2E8F0`, radius 12px, padding 16px):

Job card — RUNNING state:
- Header: [🔄 spinning cyan icon] "Chuẩn hóa số điện thoại" bold + badge "Đang chạy" (bg `#DBEAFE`, text `#06B6D4`, rounded)
- Sub: "Phạm vi: E2:E156 · 156 dòng" in `#64748B` small
- Progress bar (bg `#E2E8F0`, fill gradient `#06B6D4→#10B981`, height 8px, radius full, animated): 67%
- "67% · Còn khoảng 12 giây"
- Footer: "Bắt đầu: 14:32:15" small muted

Job card — DONE state:
- Header: [✓ green icon] "Quét hóa đơn" bold + badge "Hoàn tất" (bg `#D1FAE5`, text `#10B981`)
- "Phạm vi: A1:D45 · 45 dòng nhập thành công"
- Progress bar: 100% filled green
- "Hoàn tất lúc 14:28:03 · 0 lỗi"
- "Xem kết quả →" link text cyan

Job card — FAILED state:
- Header: [✕ red icon] "Xử lý hàng loạt" bold + badge "Thất bại" (bg `#FEE2E2`, text `#EF4444`)
- "Lỗi: File quá lớn, vui lòng thử lại"
- "Thử lại" button (outlined red)

Job card — PENDING state:
- Header: [⏳ amber icon] "Làm sạch dữ liệu cột B" bold + badge "Chờ xử lý" (bg `#FEF3C7`, text `#F59E0B`)
- "Trong hàng đợi · Vị trí: #2"

---

## Screen 6: Settings Screen
**Route:** `/settings` | **Full page, light bg `#F8FAFC`**

### Layout: Left nav 240px + Right content area

**Left Settings Nav** (bg white, border-right `#E2E8F0`, padding 20px):
- Title "Cài đặt" bold 20px
- Nav items (each: icon + text, active: bg `#EFF6FF` text `#1E3A8A` bold, left border 3px `#06B6D4`):
  - 👤 Tài khoản (active)
  - 🤖 Cài đặt AI
  - 🎨 Giao diện
  - 💬 Chatbot
  - 📤 Xuất dữ liệu
  - 📋 Lịch sử hoạt động

**Right Content — "Tài khoản" section** (padding 32px):
- Section title "Thông tin tài khoản" + divider

User profile card (bg white, border, radius 12px, padding 24px):
- Avatar (60px circle, photo placeholder)
- "Nguyễn Văn An" bold 18px
- "nguyenvan@email.com" muted
- "Chỉnh sửa ảnh" small link cyan

Form fields below (label + input pairs):
- "Họ và tên" → input value "Nguyễn Văn An"
- "Email" → input value "nguyenvan@email.com"
- "Ngôn ngữ" → dropdown "Tiếng Việt"
- "Múi giờ" → dropdown "Asia/Ho_Chi_Minh (UTC+7)"

Section "Cài đặt AI" (below, with divider):
- "Mô hình AI mặc định" → dropdown "Gemini 1.5 Pro"
- "Xác nhận trước khi áp dụng" → toggle ON (green)
- "Lưu lịch sử hội thoại" → toggle ON (green)
- "Số dòng tối đa mỗi lệnh" → input "500"

Section "Lịch sử hoạt động" table (bg white, radius 12px, border):
- Columns: Thời gian | Hành động | Bảng tính | Chi tiết
- Rows from `audit_logs`: "14:32 · Chuẩn hóa dữ liệu · Bảng lương tháng 7 · 156 ô", etc.

Footer: "Lưu thay đổi" button (bg `#1E3A8A`, white, rounded-lg)

---

## Screen 7: New Workbook Creation Modal
**Design:** Centered modal, `rgba(15,23,42,0.6)` backdrop, width: 720px**

**Modal Header** (padding 24px 28px, border-bottom):
- "✨ Tạo bảng tính mới" bold 20px `#0F172A`
- X close button

**Step 1 — Template Selection (grid 3 columns, gap 16px)**:
Label: "Chọn mẫu bảng tính" bold + "(hoặc bắt đầu từ tờ trắng)" muted

Each template card (bg white, border 2px `#E2E8F0`, radius 12px, padding 20px, cursor pointer):
- Hover/selected: border `#06B6D4`, bg `#F0FFFE`, shadow
- Top: colored icon (48px)
- Name bold `#0F172A`
- Description small `#64748B`

Templates (6 cards, 2 rows × 3):
1. [⬜ white grid icon, bg `#F8FAFC`] "Tờ trắng" — "Bắt đầu từ đầu"
2. [💰 green icon] "Bảng lương" — "Tên NV, Mã NV, Lương cơ bản, Phụ cấp, Thực nhận"
3. [📦 blue icon] "Quản lý kho" — "Mã SP, Tên SP, Số lượng, Đơn vị, Tồn kho"
4. [🧾 amber icon] "Hóa đơn nhập" — "Tên hàng, SL, Đơn giá, VAT, Thành tiền"
5. [📊 cyan icon] "Báo cáo doanh thu" — "Sản phẩm, Kỳ, Doanh thu, Lợi nhuận, Tăng trưởng"
6. [🏭 slate icon] "Kiểm kê tài sản" — "Mã tài sản, Bộ phận, Giá trị, Khấu hao, Trạng thái"

**Step 2 — Workbook Details** (below template grid, padding top 20px, border-top `#E2E8F0`):
- "Tên bảng tính" label + input (value: "Bảng lương tháng 7 - 2025", full width)
- "Mô tả" label + textarea (placeholder: "Mô tả ngắn về bảng tính này...")
- Row: "Số lượng sheets ban đầu" → number input "1" + preview chip showing sheet names

**Modal Footer** (padding 20px 28px, border-top, flex space-between):
- "Hủy" outlined gray
- "Tạo bảng tính →" (bg gradient `#1E3A8A → #06B6D4`, white bold, rounded-lg, px-8)

---

## Global UI Components (Appear Across All Screens)

### Top Navigation Brand Logo
"Smart" text in `#1E3A8A` + "Sheet AI" in `#06B6D4` — font weight 800 — with a 20px icon: a grid of 4 squares where top-right square is replaced by a cyan sparkle/AI star

### Notification Toast (bottom-left, slide-up animation)
- Success: bg `#D1FAE5`, border-left 4px `#10B981`, icon ✓ green
- Error: bg `#FEE2E2`, border-left 4px `#EF4444`, icon ✕ red
- Info: bg `#DBEAFE`, border-left 4px `#06B6D4`, icon ℹ cyan

### Data Type Icons in Column Headers
- Text columns: "T" in a small badge, color `#64748B`
- Number columns: "#" in a small badge, color `#10B981`
- Date columns: calendar icon, color `#06B6D4`
- Boolean columns: toggle icon, color `#F59E0B`

### AI Status Indicator (Right sidebar header, small dot)
- Online/Ready: pulsing green dot `#10B981`
- Processing: pulsing cyan dot `#06B6D4` with spin animation
- Error: red dot `#EF4444`

### Voice Input Button (In AI Chatbot panel)
- Default: round button bg `#1E3A8A`, white mic icon
- Active/Recording: bg `#EF4444`, pulsing glow ring animation in red, mic icon white
- Processing: bg `#F59E0B`, spinner

---

## Presentation Layout Instructions for Stitch
Generate **7 separate screens** as individual artboards or frames, each at **1440 × 900px** resolution:
1. `dashboard` — Home/Dashboard
2. `editor` — Main Spreadsheet Editor (most complex, most important)
3. `scan` — Document Upload & Scan (shown as modal over editor)
4. `diff_preview` — AI Diff Preview Modal
5. `ai_jobs` — AI Job Status Panel
6. `settings` — Settings Page
7. `new_workbook` — New Workbook Creation Modal

All screens must use **identical** design tokens (colors, fonts, spacing, radius) from the Design System section above. Vietnamese text must appear on ALL screens.