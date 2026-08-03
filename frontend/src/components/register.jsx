import React, { useState } from 'react';
import { Mail, Lock, Eye, EyeOff, User, Sparkles, ShieldCheck } from 'lucide-react';
import '../App.css';
import smartsheetLogo from "../assets/smartsheet.png"

const RegisterPage = ({ onNavigateToLogin }) => {
    // --- STATES ---
    const [fullName, setFullName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [showPassword, setShowPassword] = useState(false);
    const [showConfirmPassword, setShowConfirmPassword] = useState(false);
    const [agreeTerms, setAgreeTerms] = useState(false);
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);

    // --- SUBMIT HANDLER ---
    const handleRegisterSubmit = async (e) => {
        e.preventDefault();
        setError('');
        setLoading(true);

        if (!fullName || !email || !password || !confirmPassword) {
            setError('Vui lòng nhập đầy đủ thông tin.');
            setLoading(false);
            return;
        }

        if (password !== confirmPassword) {
            setError('Mật khẩu xác nhận không khớp.');
            setLoading(false);
            return;
        }

        if (!agreeTerms) {
            setError('Vui lòng đồng ý với Điều khoản & Chính sách bảo mật.');
            setLoading(false);
            return;
        }

        try {
            const response = await fetch('http://localhost:8000/api/v1/auth/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    full_name: fullName,
                    email: email,
                    password: password,
                }),
            });

            const data = await response.json();

            if (!response.ok) {
                const errorDetail = typeof data.detail === 'string'
                    ? data.detail
                    : 'Đăng ký thất bại. Vui lòng thử lại.';
                throw new Error(errorDetail);
            }

            onNavigateToLogin();

        } catch (err) {
            setError(err.message || 'Không thể kết nối tới máy chủ. Vui lòng thử lại sau.');
        } finally {
            setLoading(false);
        }
    };

    const handleGoogleRegister = () => {
        alert('Đang kết nối tới Google Auth...');
        // window.location.href = 'http://localhost:8000/api/v1/auth/google';
    };

    const handleSSORegister = () => {
        alert('Đang kết nối tới SSO Enterprise...');
        // window.location.href = 'http://localhost:8000/api/v1/auth/sso';
    };

    return (
        <div className="login-container">
            <div className="login-box">

                {/* ================= BÊN TRÁI: INTRO & FEATURES ================= */}
                <div className="login-left">
                    <div className="left-content">
                        <h2>Khai phá sức mạnh dữ liệu với SmartSheet AI</h2>
                        <p>
                            Nền tảng bảng tính thông minh giúp tự động hóa quy trình, phân tích dữ liệu chuyên sâu và hỗ trợ ra quyết định bằng trí tuệ nhân tạo.
                        </p>

                        <div className="feature-cards">
                            <div className="f-card">
                                <Sparkles size={24} className="icon-blue" />
                                <h4>AI Phân tích</h4>
                                <p>Tự động đề xuất công thức và xu hướng.</p>
                            </div>
                            <div className="f-card">
                                <ShieldCheck size={24} className="icon-blue" />
                                <h4>Bảo mật tối đa</h4>
                                <p>Mã hóa dữ liệu doanh nghiệp chuẩn quốc tế.</p>
                            </div>
                        </div>
                    </div>
                </div>

                {/* ================= BÊN PHẢI: FORM ĐĂNG KÝ ================= */}
                <div className="login-right">
                    <div className="right-content">

                        {/* Logo */}
                        <div className="image-logo">
                            <img src={smartsheetLogo} />
                        </div>

                        <h3>Tạo tài khoản mới</h3>
                        <p className="subtitle">Tham gia SmartSheet AI ngay hôm nay và mở khóa tiềm năng dữ liệu của bạn.</p>

                        {/* Thông báo Lỗi */}
                        {error && <div className="error-message">{error}</div>}

                        {/* Form */}
                        <form onSubmit={handleRegisterSubmit}>

                            {/* Field Full Name */}
                            <div className="input-group">
                                <label>Họ và tên</label>
                                <div className="input-wrapper">
                                    <input
                                        type="text"
                                        placeholder="Nguyễn Văn A"
                                        value={fullName}
                                        onChange={(e) => setFullName(e.target.value)}
                                        required
                                    />
                                    <User className="input-icon-right" size={18} />
                                </div>
                            </div>

                            {/* Field Email */}
                            <div className="input-group">
                                <label>Email</label>
                                <div className="input-wrapper">
                                    <input
                                        type="email"
                                        placeholder="name@company.com"
                                        value={email}
                                        onChange={(e) => setEmail(e.target.value)}
                                        required
                                    />
                                    <Mail className="input-icon-right" size={18} />
                                </div>
                            </div>

                            {/* Field Password */}
                            <div className="input-group">
                                <label>Mật khẩu</label>
                                <div className="input-wrapper">
                                    <input
                                        type={showPassword ? 'text' : 'password'}
                                        placeholder="••••••••"
                                        value={password}
                                        onChange={(e) => setPassword(e.target.value)}
                                        required
                                    />
                                    <button
                                        type="button"
                                        className="icon-button-right"
                                        onClick={() => setShowPassword(!showPassword)}
                                        tabIndex={-1}
                                    >
                                        {showPassword ? <EyeOff size={18} /> : <Eye size={18} />}
                                    </button>
                                </div>
                            </div>

                            {/* Field Confirm Password */}
                            <div className="input-group">
                                <label>Xác nhận mật khẩu</label>
                                <div className="input-wrapper">
                                    <input
                                        type={showConfirmPassword ? 'text' : 'password'}
                                        placeholder="••••••••"
                                        value={confirmPassword}
                                        onChange={(e) => setConfirmPassword(e.target.value)}
                                        required
                                    />
                                    <button
                                        type="button"
                                        className="icon-button-right"
                                        onClick={() => setShowConfirmPassword(!showConfirmPassword)}
                                        tabIndex={-1}
                                    >
                                        {showConfirmPassword ? <EyeOff size={18} /> : <Eye size={18} />}
                                    </button>
                                </div>
                            </div>

                            {/* Checkbox Terms */}
                            <div className="form-actions">
                                <label className="checkbox-container">
                                    <input
                                        type="checkbox"
                                        checked={agreeTerms}
                                        onChange={(e) => setAgreeTerms(e.target.checked)}
                                    />
                                    <span className="checkmark"></span>
                                    Tôi đồng ý với <a href="#terms" className="link-primary">Điều khoản & Điều kiện</a> và <a href="#privacy" className="link-primary">Chính sách bảo mật</a>
                                </label>
                            </div>

                            {/* Nút Submit */}
                            <button
                                type="submit"
                                className="btn-primary"
                                disabled={loading}
                            >
                                {loading ? 'Đang xử lý...' : 'Tạo tài khoản ➔'}
                            </button>
                        </form>

                        {/* Phân cách */}
                        <div className="separator">
                            <span>Hoặc tiếp tục với</span>
                        </div>

                        {/* Google Auth */}
                        <button
                            type="button"
                            className="btn-google"
                            onClick={handleGoogleRegister}
                        >
                            <img
                                src="https://authjs.dev/img/providers/google.svg"
                                alt="Google"
                                width={18}
                            />
                            Đăng ký với Google
                        </button>

                        {/* Footer Login */}
                        <p className="footer-text">
                            Đã có tài khoản? <a href="#login" onClick={(e) => { e.preventDefault(); onNavigateToLogin(); }}>Đăng nhập</a>
                        </p>

                    </div>
                </div>

            </div>
        </div>
    );
};

export default RegisterPage;
