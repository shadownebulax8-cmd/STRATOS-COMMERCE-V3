import { useEffect, useState } from 'react';

export default function AdminDashboard() {
  const [analytics, setAnalytics] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/v1/analytics/overview', {
      headers: { Authorization: 'Bearer demo-token' },
    })
      .then((res) => res.json())
      .then((data) => setAnalytics(data))
      .catch(() => setAnalytics({ error: 'Unable to reach backend' }));
  }, []);

  return (
    <main style={{ padding: '2rem', fontFamily: 'Arial, sans-serif', background: '#f4f7fb', minHeight: '100vh', color: '#111827' }}>
      <h1 style={{ marginBottom: '0.25rem' }}>Admin Analytics Dashboard</h1>
      <p style={{ marginTop: 0, marginBottom: '1.5rem', color: '#4b5563' }}>Operational and inventory insights for merchants, ops teams, and platform administrators.</p>

      <section style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: '1rem', marginBottom: '1.5rem' }}>
        <div style={{ background: 'white', padding: '1rem', borderRadius: '12px', boxShadow: '0 4px 12px rgba(0,0,0,0.06)' }}>
          <strong>Orders</strong>
          <div style={{ fontSize: '1.5rem', marginTop: '0.4rem' }}>128</div>
        </div>
        <div style={{ background: 'white', padding: '1rem', borderRadius: '12px', boxShadow: '0 4px 12px rgba(0,0,0,0.06)' }}>
          <strong>Revenue</strong>
          <div style={{ fontSize: '1.5rem', marginTop: '0.4rem' }}>$8,420</div>
        </div>
        <div style={{ background: 'white', padding: '1rem', borderRadius: '12px', boxShadow: '0 4px 12px rgba(0,0,0,0.06)' }}>
          <strong>Tenants</strong>
          <div style={{ fontSize: '1.5rem', marginTop: '0.4rem' }}>3</div>
        </div>
      </section>

      <pre style={{ background: '#111827', color: '#f9fafb', padding: '1rem', borderRadius: '8px', overflowX: 'auto' }}>
        {analytics ? JSON.stringify(analytics, null, 2) : 'Loading analytics...'}
      </pre>
    </main>
  );
}
