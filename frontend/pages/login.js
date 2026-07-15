import { useState } from 'react';

export default function LoginPage() {
  const [state, setState] = useState({ email: '', password: '' });

  const handleSubmit = (event) => {
    event.preventDefault();
    alert(`Login requested for ${state.email}`);
  };

  return (
    <main style={{ minHeight: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center', background: 'linear-gradient(135deg, #07111f, #13233b)', color: 'white' }}>
      <form onSubmit={handleSubmit} style={{ background: 'rgba(19, 35, 59, 0.95)', padding: '2rem', borderRadius: '16px', minWidth: '320px', boxShadow: '0 20px 45px rgba(0,0,0,0.25)' }}>
        <h2 style={{ marginTop: 0 }}>Merchant Login</h2>
        <p style={{ color: '#cbd5e1', marginBottom: '1rem' }}>Access your tenant dashboard and operations console.</p>
        <input placeholder="Email" style={{ display: 'block', width: '100%', marginBottom: '1rem', padding: '0.8rem', borderRadius: '8px', border: '1px solid #475569' }} value={state.email} onChange={(e) => setState({ ...state, email: e.target.value })} />
        <input type="password" placeholder="Password" style={{ display: 'block', width: '100%', marginBottom: '1rem', padding: '0.8rem', borderRadius: '8px', border: '1px solid #475569' }} value={state.password} onChange={(e) => setState({ ...state, password: e.target.value })} />
        <button type="submit" style={{ width: '100%', padding: '0.85rem', background: '#4f46e5', color: 'white', border: 'none', borderRadius: '8px', cursor: 'pointer' }}>Login</button>
      </form>
    </main>
  );
}
