import React, { useState } from 'react';
import { 
  Search, Bell, Settings, User, Plus, FileText, Folder, Share2, 
  Archive, Trash2, TrendingUp, Brain, Zap, Clock, ChevronRight,
  BarChart3, Database, Cloud, CheckCircle
} from 'lucide-react';
import '../App.css';
import smartsheetLogo from "../assets/smartsheet.png"

const Dashboard = ({ onLogout }) => {
  const [searchQuery, setSearchQuery] = useState('');

  const recentSpreadsheets = [
    { name: 'Bảng lương tháng 7', time: 'Cập nhật 2 giờ trước', icon: FileText },
    { name: 'Báo cáo kho bãi Q2', time: 'Dữ liệu từ 3 kho, AI Insight', icon: Database },
    { name: 'Hóa đơn nhập hàng', time: 'Gần đây: VinMart+', icon: FileText },
    { name: 'Doanh thu 2025', time: 'Dự báo tăng 12%', icon: TrendingUp },
    { name: 'Kiểm kê sản phẩm', time: '1,240 mặt hàng', icon: BarChart3 },
    { name: 'Chi phí vận hành', time: 'Cần tối ưu hóa AI', icon: FileText },
  ];

  const quickActions = [
    { name: 'Tạo bảng mới', icon: Plus, color: '#3b82f6' },
    { name: 'Quét hóa đơn', icon: Zap, color: '#10b981' },
    { name: 'Nhập file Excel', icon: FileText, color: '#f59e0b' },
    { name: 'Hỏi trợ lý AI', icon: Brain, color: '#8b5cf6' },
  ];

  const recentActivities = [
    { action: 'Bạn đã phê duyệt Bảng lương tháng 7', time: '10 phút trước', type: 'approval' },
    { action: 'AI hoàn thành phân tích doanh thu 2025', time: '45 phút trước', type: 'ai' },
    { action: 'Minh Nguyễn đã chỉnh sửa Báo cáo kho', time: '2 giờ trước', type: 'edit' },
    { action: 'Bạn đã chia sẻ Hóa đơn nhập hàng', time: 'Hôm qua', type: 'share' },
  ];

  const navItems = [
    { name: 'Bảng tính của tôi', icon: FileText, active: true },
    { name: 'Thư mục dự án', icon: Folder, active: false },
    { name: 'Tệp đã chia sẻ', icon: Share2, active: false },
    { name: 'Lưu trữ', icon: Archive, active: false },
    { name: 'Thùng rác', icon: Trash2, active: false },
  ];

  return (
    <div className="dashboard-container">
      {/* ================= SIDEBAR ================= */}
      <div className="sidebar">
        <div className="sidebar-header">
          <div className="sidebar-logo">
            <img src={smartsheetLogo} alt="SmartSheet AI" />
            <div className="logo-text">
              <span className="logo-title">SmartSheet AI</span>
              <span className="logo-tagline">Giải pháp dữ liệu thông minh</span>
            </div>
          </div>
        </div>

        <nav className="sidebar-nav">
          {navItems.map((item, index) => (
            <div key={index} className={`nav-item ${item.active ? 'active' : ''}`}>
              <item.icon size={20} />
              <span>{item.name}</span>
              {item.active && <ChevronRight size={16} className="nav-arrow" />}
            </div>
          ))}
        </nav>

        <div className="sidebar-footer">
          <button className="btn-create-new">
            <Plus size={20} />
            <span>Tạo bảng tính mới</span>
          </button>
        </div>
      </div>

      {/* ================= MAIN CONTENT ================= */}
      <div className="main-content">
        {/* ================= TOP BAR ================= */}
        <div className="top-bar">
          <div className="search-bar">
            <Search size={20} className="search-icon" />
            <input
              type="text"
              placeholder="Tìm kiếm bảng tính..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
            />
          </div>

          <div className="top-bar-actions">
            <button className="btn-upgrade">
              <Zap size={16} />
              Nâng cấp AI
            </button>
            <button className="btn-icon">
              <Bell size={20} />
            </button>
            <button className="btn-icon">
              <Settings size={20} />
            </button>
            <button className="btn-profile">
              <User size={20} />
            </button>
          </div>
        </div>

        {/* ================= DASHBOARD CONTENT ================= */}
        <div className="dashboard-content">
          {/* ================= SUMMARY CARDS ================= */}
          <div className="summary-cards">
            <div className="summary-card">
              <div className="card-icon card-icon-blue">
                <FileText size={24} />
              </div>
              <div className="card-content">
                <div className="card-label">TỔNG BẢNG TÍNH</div>
                <div className="card-value">24</div>
                <div className="card-trend positive">+3 tuần này</div>
              </div>
            </div>

            <div className="summary-card">
              <div className="card-icon card-icon-purple">
                <Brain size={24} />
              </div>
              <div className="card-content">
                <div className="card-label">AI DÙNG</div>
                <div className="card-value">1240/2000</div>
                <div className="card-trend">62% sử dụng</div>
              </div>
            </div>

            <div className="summary-card">
              <div className="card-icon card-icon-green">
                <CheckCircle size={24} />
              </div>
              <div className="card-content">
                <div className="card-label">TÀI LIỆU QUÉT</div>
                <div className="card-value">87</div>
                <div className="card-trend">OCR sẵn sàng</div>
              </div>
            </div>

            <div className="summary-card">
              <div className="card-icon card-icon-orange">
                <Cloud size={24} />
              </div>
              <div className="card-content">
                <div className="card-label">ĐỒNG BỘ</div>
                <div className="card-value">2 phút trước</div>
                <div className="card-trend">Cloud Node: SG-1</div>
              </div>
            </div>
          </div>

          {/* ================= RECENT SPREADSHEETS ================= */}
          <div className="section">
            <div className="section-header">
              <h2>Bảng tính gần đây</h2>
              <a href="#view-all" className="view-all">Xem tất cả</a>
            </div>
            <div className="spreadsheets-grid">
              {recentSpreadsheets.map((sheet, index) => (
                <div key={index} className="spreadsheet-card">
                  <div className="spreadsheet-icon">
                    <sheet.icon size={24} />
                  </div>
                  <div className="spreadsheet-info">
                    <h3>{sheet.name}</h3>
                    <p>{sheet.time}</p>
                  </div>
                  <ChevronRight size={16} className="spreadsheet-arrow" />
                </div>
              ))}
            </div>
          </div>

          {/* ================= QUICK ACTIONS ================= */}
          <div className="section">
            <h2>Hành động nhanh</h2>
            <div className="quick-actions">
              {quickActions.map((action, index) => (
                <button key={index} className="quick-action-btn" style={{ '--action-color': action.color }}>
                  <action.icon size={24} />
                  <span>{action.name}</span>
                </button>
              ))}
            </div>
          </div>

          {/* ================= AI ASSISTANT ================= */}
          <div className="ai-assistant-section">
            <div className="ai-assistant-content">
              <div className="ai-icon">
                <Brain size={32} />
              </div>
              <div className="ai-text">
                <h3>Tăng tốc xử lý với Trợ lý AI</h3>
                <p>Sử dụng ngôn ngữ tự nhiên để tạo công thức phức tạp hoặc phân tích xu hướng dữ liệu ngay lập tức.</p>
              </div>
              <div className="ai-actions">
                <button className="btn-primary-sm">Thử ngay</button>
                <button className="btn-secondary-sm">Tìm hiểu thêm</button>
              </div>
            </div>
          </div>

          {/* ================= RECENT ACTIVITIES ================= */}
          <div className="section">
            <h2>Hoạt động gần đây</h2>
            <div className="activities-list">
              {recentActivities.map((activity, index) => (
                <div key={index} className="activity-item">
                  <div className="activity-icon">
                    {activity.type === 'approval' && <CheckCircle size={16} />}
                    {activity.type === 'ai' && <Brain size={16} />}
                    {activity.type === 'edit' && <FileText size={16} />}
                    {activity.type === 'share' && <Share2 size={16} />}
                  </div>
                  <div className="activity-content">
                    <p>{activity.action}</p>
                    <span className="activity-time">{activity.time}</span>
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* ================= FOOTER ================= */}
          <div className="dashboard-footer">
            <p>© 2024 SmartSheet AI. Đã kết nối hệ thống.</p>
            <div className="footer-links">
              <a href="#status">Trạng thái</a>
              <a href="#api">Tài liệu API</a>
              <a href="#support">Hỗ trợ</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
