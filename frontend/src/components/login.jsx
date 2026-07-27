import React, { useState } from 'react';
import { Mail, Lock, Eye, EyeOff, Sparkles, ShieldCheck } from 'lucide-react';
import '../App.css';
import smartsheetLogo from "../assets/smartsheet.png"
const LoginPage = () => {
    // --- STATES ---
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [showPassword, setShowPassword] = useState(false);
    const [rememberMe, setRememberMe] = useState(false);
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);

    // --- SUBMIT HANDLER ---
    const handleLoginSubmit = async (e) => {
        e.preventDefault();
        setError('');
        setLoading(true);

        if (!email || !password) {
            setError('Vui lòng nhập đầy đủ Email và Mật khẩu.');
            setLoading(false);
            return;
        }

        try {
            // Option 1: Nếu Backend FastAPI dùng OAuth2PasswordRequestForm (chuẩn form-urlencoded)
            const formData = new URLSearchParams();
            formData.append('username', email); // FastAPI OAuth2 mặc định dùng field 'username'
            formData.append('password', password);

            // const response = await fetch('http://localhost:8000/api/v1/auth/login', {
            //     method: 'POST',
            //     headers: {
            //         'Content-Type': 'application/x-www-form-urlencoded',
            //     },
            //     body: formData,
            // });

            // Option 2: Bỏ comment đoạn này nếu Backend nhận JSON Payload { "email": "...", "password": "..." }
            const response = await fetch('http://localhost:8000/api/v1/auth/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    email: email,
                    password: password,
                }),
            });

            const data = await response.json();

            // Kiểm tra phản hồi từ Backend
            if (!response.ok) {
                // Lấy chi tiết thông báo lỗi từ FastAPI trả về
                const errorDetail = typeof data.detail === 'string'
                    ? data.detail
                    : 'Email hoặc mật khẩu không chính xác.';
                throw new Error(errorDetail);
            }

            // Đăng nhập thành công -> Lưu Token vào LocalStorage
            console.log('Login success:', data);
            if (data.access_token) {
                localStorage.setItem('access_token', data.access_token);
                if (data.refresh_token) {
                    localStorage.setItem('refresh_token', data.refresh_token);
                }
            }

            alert('Đăng nhập thành công! 🎉');

            // Chuyển hướng trang (ví dụ: sang Dashboard)
            // window.location.href = '/dashboard';

        } catch (err) {
            setError(err.message || 'Không thể kết nối tới máy chủ. Vui lòng thử lại sau.');
        } finally {
            setLoading(false);
        }
    };

    const handleGoogleLogin = () => {
        alert('Đang kết nối tới Google Auth...');
        // window.location.href = 'http://localhost:8000/api/v1/auth/google';
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

                {/* ================= BÊN PHẢI: FORM ĐĂNG NHẬP ================= */}
                <div className="login-right">
                    <div className="right-content">

                        {/* Logo */}
                        <div className="image-logo">
                            <img src={smartsheetLogo} />
                        </div>

                        <h3>SmartSheet AI</h3>
                        <p className="subtitle">Chào mừng bạn trở lại. Vui lòng đăng nhập.</p>

                        {/* Thông báo Lỗi */}
                        {error && <div className="error-message">{error}</div>}

                        {/* Form */}
                        <form onSubmit={handleLoginSubmit}>

                            {/* Field Email */}
                            <div className="input-group">
                                <label>Email công việc</label>
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

                            {/* Field Mật khẩu */}
                            <div className="input-group">
                                <div className="label-row">
                                    <label>Mật khẩu</label>
                                    <a href="#forgot" className="forgot-pass">Quên mật khẩu?</a>
                                </div>
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

                            {/* Checkbox Remember Me */}
                            <div className="form-actions">
                                <label className="checkbox-container">
                                    <input
                                        type="checkbox"
                                        checked={rememberMe}
                                        onChange={(e) => setRememberMe(e.target.checked)}
                                    />
                                    <span className="checkmark"></span>
                                    Ghi nhớ đăng nhập
                                </label>
                            </div>

                            {/* Nút Submit */}
                            <button
                                type="submit"
                                className="btn-primary"
                                disabled={loading}
                            >
                                {loading ? 'Đang xử lý...' : 'Đăng nhập ➔'}
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
                            onClick={handleGoogleLogin}
                        >
                            <img
                                src="https://authjs.dev/img/providers/google.svg"
                                alt="Google"
                                width={18}
                            />
                            Đăng nhập với Google
                        </button>

                        {/* Footer Sign up */}
                        <p className="footer-text">
                            Chưa có tài khoản? <a href="#register">Đăng ký ngay</a>
                        </p>

                    </div>
                </div>

            </div>
        </div>
    );
};

export default LoginPage;