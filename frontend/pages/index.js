import Head from 'next/head';

export default function Home() {
  return (
    <>
      <Head>
        <title>STRATOS-COMMERCE V3 Dashboard</title>
        <meta name="description" content="A next-generation multi-tenant marketplace dashboard scaffold" />
      </Head>
      <main style={{ fontFamily: 'Arial, sans-serif', padding: '2rem', background: '#07111f', color: '#f5f7ff', minHeight: '100vh' }}>
        <h1>STRATOS-COMMERCE V3</h1>
        <p>Multi-tenant B2B marketplace dashboard scaffold</p>
        <ul>
          <li>Merchant overview</li>
          <li>Inventory analytics</li>
          <li>Escrow payout insights</li>
          <li>Real-time operations</li>
        </ul>
      </main>
    </>
  );
}
