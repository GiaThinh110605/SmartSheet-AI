import './App.css'
import LoginPage from './components/login'
import RegisterPage from './components/register'
import Dashboard from './components/Dashboard'
import { useState } from 'react'

function App() {
  const [currentPage, setCurrentPage] = useState('login')

  const navigateToRegister = () => setCurrentPage('register')
  const navigateToLogin = () => setCurrentPage('login')
  const navigateToDashboard = () => setCurrentPage('dashboard')
  const navigateToLoginFromDashboard = () => setCurrentPage('login')

  return (
    <>
      {currentPage === 'login' ? (
        <LoginPage onNavigateToRegister={navigateToRegister} onNavigateToDashboard={navigateToDashboard} />
      ) : currentPage === 'register' ? (
        <RegisterPage onNavigateToLogin={navigateToLogin} />
      ) : (
        <Dashboard onLogout={navigateToLoginFromDashboard} />
      )}
    </>
  )
}

export default App
