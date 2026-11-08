import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

function Login() {
  const [formData, setFormData] = useState({ username: '', password: '' });
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const params = new URLSearchParams();
      params.append('username', formData.username);
      params.append('password', formData.password);
      const res = await axios.post('http://localhost:8001/api/auth/login', params);
      localStorage.setItem('token', res.data.access_token);
      navigate('/');
    } catch (err) {
      alert('Login failed');
    }
  };

  return (
    <div style={{ background: '#000', color: '#fff', height: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
      <form onSubmit={handleSubmit} style={{ background: '#333', padding: '2rem', borderRadius: '10px' }}>
        <h2>Sign In</h2>
        <input type="text" placeholder="Username" onChange={e => setFormData({...formData, username: e.target.value})} /><br/>
        <input type="password" placeholder="Password" onChange={e => setFormData({...formData, password: e.target.value})} /><br/>
        <button type="submit">Sign In</button>
      </form>
    </div>
  );
}
export default Login;
