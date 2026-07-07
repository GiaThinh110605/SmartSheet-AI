# MÔ-ĐUN 1: CORE SPREADSHEET ENGINE (Nền tảng bảng tính)
Đây là phần khung xương giúp ứng dụng hoạt động mượt mà như một trình quản lý Excel thực thụ.
* 1.1. Grid Rendering & Virtual Scroll: Sử dụng thư viện mã nguồn mở (Luckysheet/FortuneSheet) để hiển thị hàng ngàn dòng/cột mà không bị lag trình duyệt nhờ kỹ thuật rendering chỉ những ô đang xuất hiện trên màn hình.
* 1.2. Biến đổi Tọa độ dữ liệu (Cell-Coordinate Mapping): Quản lý trạng thái dữ liệu của từng ô theo mô hình tọa độ hàng và cột (row_index, col_index). Khi F5 trang, dữ liệu tự động đồng bộ từ PostgreSQL.
* 1.3. Quản lý cấu trúc Cột (Dynamic Column Definition): Định nghĩa tên tiêu đề cột (Header Name) và ép kiểu dữ liệu (Data Type như Text, Number, Date) cho từng cột. Đây là cơ sở để AI đọc hiểu cấu trúc bảng.
* 1.4. Xuất/Nhập file (Import/Export): Cho phép người dùng upload file .xlsx hoặc .csv có sẵn để hệ thống phân tách dữ liệu vào Database, và ngược lại, cho phép tải bảng tính hiện tại về máy dưới dạng file Excel chuẩn.
* 1.5 Vẽ trên bảng tính
* 1.6 Dữ liệu: sắp xếp tăng dần, sắp xếp giảm dần, loại bỏ nội dung trùng lặp
* 1.7 Chèn: thêm bảng, hình ảnh, những hình có sẵn (hình vuông, tròn …)

# MÔ-ĐUN 2: COMPANION CHATBOT AI (Trợ lý đồng hành)
Khung chat nằm cố định bên phải (tỷ lệ 25% màn hình), giao tiếp thời gian thực qua WebSockets hoặc Long-Polling.
* 2.1. Đọc hiểu ngữ cảnh bảng (Context-Aware Chat): Chatbot tự động nắm bắt file này đang có những cột nào, kiểu dữ liệu gì mà không cần người dùng mô tả lại cấu trúc bảng.
* 2.2. Nhập liệu bằng giọng nói (Voice-to-Text Input): Tích hợp Web Speech API trên trình duyệt, cho phép nhân viên hiện trường hoặc người lười gõ phím bấm nói để AI tự động chuyển thành câu lệnh văn bản.
* 2.3. Quản lý lịch sử hội thoại (Session Memory): Lưu lại luồng trò chuyện của phiên làm việc giúp AI hiểu được các câu lệnh mang tính kế thừa (Ví dụ: "Sửa lại tên" -> "Ý tôi là viết hoa tất cả chữ cái đầu").
MÔ-ĐUN 3: DATA AUTO-PROCESSING & PREVIEW (Xử lý và Xem trước dữ liệu)
Tính năng "vũ khí bí mật" giúp nâng tầm ứng dụng.
* 3.1. Nhập liệu tự động từ văn bản tự nhiên (Chat-to-Sheet): AI tự động bóc tách thông tin từ một câu nói hỗn độn của nhân viên (ví dụ: "Anh Nam mua 3 cái ghế chưa trả tiền") để gom vào các cột tương ứng (Khách hàng, Số lượng, Sản phẩm, Trạng thái).
* 3.2. Chế độ xem trước thay đổi (Visual Diff Preview Mode): Trước khi ghi đè vào Database, hệ thống sinh ra một "bản nháp" (Pending State) hiển thị trực quan trên bảng tính:
    * Ô bị thay đổi sẽ chuyển màu Đỏ/Gạch ngang cho giá trị cũ.
    * Màu Xanh lá cho giá trị mới do AI đề xuất.
* 3.3. Xác thực dữ liệu tập trung (Human-in-the-loop Commit): Cung cấp 2 nút [Áp dụng] và [Hủy] dưới chân khung chat để người dùng kiểm soát hành động của AI, ngăn chặn tuyệt đối lỗi ảo giác (Hallucination) làm hỏng dữ liệu gốc.
* 3.4. Chuẩn hóa dữ liệu hàng loạt (Bulk Data Cleaning): Tự động quét hàng loạt ô trong một cột được chỉ định để sửa lỗi chính tả, chuẩn hóa định dạng ngày tháng (DD/MM/YYYY) hoặc định dạng số điện thoại chuẩn Việt Nam (thêm số 0 ở đầu).

# MÔ-ĐUN 4: NATURAL LANGUAGE INTELLIGENCE (Trích xuất & Truy vấn thông minh)
Giúp người "mù" công thức vẫn làm chủ được dữ liệu nâng cao.
* 4.1. Hàm AI Tự tạo (Custom AI Functions):
    * =AI_EXTRACT(cell, "yêu cầu"): Trích xuất thông tin đặc trưng (Mã đơn hàng, Mã số thuế, Địa chỉ) ra khỏi một chuỗi text dài.
    * =AI_CLASSIFY(cell, "danh sách nhãn"): Gắn nhãn tự động cho dữ liệu (Phân loại chi tiêu, phân loại đánh giá của khách hàng thành Tích cực/Tiêu cực).
* 4.2. Hỏi đáp trên dữ liệu (Natural Language to Query): Người dùng gõ câu hỏi: "Ai là người mua nhiều hàng nhất trong tháng 5?", Backend AI dịch câu hỏi thành logic lọc (Filter/Query), tự động ẩn các dòng không liên quan và làm nổi bật dòng kết quả chính xác.
* 4.3. Tự động trực quan hóa (Natural Language to Chart): Khi người dùng yêu cầu xem xu hướng hoặc so sánh, AI tự động chọn loại biểu đồ phù hợp (Biểu đồ cột, biểu đồ đường, hình tròn) và vẽ trực tiếp lên một phân khu Dashboard riêng biệt.

# MÔ-ĐUN 5: IMAGE INTELLIGENCE & DOCUMENT SCANNING (Trích xuất từ hình ảnh)
Tận dụng sức mạnh của Vision-Language Model để số hóa quy trình nhập liệu thủ công.
* 5.1. Quét hóa đơn/Chứng từ (Scan-to-Sheet): Cho phép kéo thả ảnh chụp hóa đơn GTGT, phiếu nhập kho, biên lai. AI sử dụng OCR nâng cao kết hợp phân tích layout cấu trúc để chuyển đổi toàn bộ danh mục sản phẩm thành các hàng và cột ngăn nắp trong bảng tính.
* 5.2. Nhận diện trạng thái vật lý qua ảnh: Tích hợp cho các ngành Logistics/Kho bãi; nhân viên chụp ảnh kệ hàng bị thiếu hoặc ảnh sản phẩm lỗi, AI tự động nhận diện tên sản phẩm, đếm số lượng lỗi và điền thẳng vào biên bản báo cáo dạng bảng trên Web.

# MÔ-ĐUN 6: BACKEND & COMPUTE OPTIMIZATION (Tối ưu hóa hệ thống - MLOps)
Phần tính năng ẩn dưới Backend chứng minh bạn là một AI Engineer có kiến thức sâu về hệ thống.
* 6.1. Gom cụm Request (Smart Request Batching): Khi người dùng áp dụng tính năng AI cho hàng trăm dòng bằng cách kéo chuột, Backend (FastAPI) sẽ tự động gộp (batch) các dòng đó lại thành 1 request duy nhất sang Gemini API nhằm tiết kiệm 90% chi phí gọi API và tránh lỗi nghẽn băng thông (Rate Limit).
* 6.2. Bộ nhớ đệm dữ liệu tính toán (Response Caching): Tích hợp Redis hoặc lưu trữ trạng thái computed_value ở Postgres. Nếu dữ liệu ở ô gốc không đổi, hệ thống sẽ lấy ngay kết quả cũ mà không gọi lại API AI, giúp tối ưu tốc độ phản hồi xuống < 50ms.
* 6.3. Xử lý hàng đợi bất đồng bộ (Background Tasks Queue): Với các tác vụ nặng như xử lý file Excel 10,000 dòng hoặc scan cùng lúc 20 ảnh hóa đơn, hệ thống đẩy vào hàng đợi Celery + Redis để xử lý ngầm dưới Backend, giúp giao diện Frontend của người dùng không bị đóng băng (freezing).

