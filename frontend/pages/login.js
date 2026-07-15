import { useState } from 'react';

export default function LoginPage() {
  const [state, setState] = useState({ email: '', password: '' });

  const handleSubmit = (event) => {
    event.preventDefault();
    alert(`Login requested for ${state.email}`);
  };

  return (
    <main style={{ minHeight: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center', background: '#07111f', color: 'white' }}>
      <form onSubmit={handleSubmit} style={{ background: '#13233b', padding: '2rem', borderRadius: '12px', minWidth: '320px' }}>
        <h2>Merchant Login</h2>
        <input placeholder="Email" style={{ display: 'block', width: '100%', marginBottom: '1rem', padding: '0.75rem' }} value={state.email} onChange={(e) => setState({ ...state, email: e.target.value })} />
        <input type="password" placeholder="Password" style={{ display: 'block', width: '100%', marginBottom: '1rem', padding: '0.75rem' }} value={state.password} onChange={(e) => setState({ ...state, password: e.target.value })} />
        <button type="submit" style={{ width: '100%', padding: '0.8rem', background: '#4f46e5', color: 'white', border: 'none', borderRadius: '6px' }}>Login</button>
      </form>
    </main>
  );
}
