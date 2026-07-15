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
    <main style={{ padding: '2rem', fontFamily: 'Arial, sans-serif', background: '#f4f7fb', minHeight: '100vh' }}>
      <h1>Admin Analytics Dashboard</h1>
      <p>Operational and inventory insights for merchants and platform ops.</p>
      <pre style={{ background: '#111827', color: '#f9fafb', padding: '1rem', borderRadius: '8px' }}>
        {analytics ? JSON.stringify(analytics, null, 2) : 'Loading analytics...'}
      </pre>
    </main>
  );
}
