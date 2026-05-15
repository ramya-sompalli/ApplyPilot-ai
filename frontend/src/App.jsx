// frontend/src/App.jsx
import { useEffect, useState } from "react"

function App() {
  const [status, setStatus] = useState("checking...")

  useEffect(() => {
    fetch("http://127.0.0.1:8000/health")   // ← changed from localhost to 127.0.0.1
      .then(res => res.json())
      .then(data => setStatus(data.status))
      .catch(() => setStatus("❌ Cannot reach backend — check CORS"))
  }, [])

  return (
    <div style={{ padding: "40px", fontFamily: "sans-serif" }}>
      <h1>AI Job Autopilot</h1>
      <p>Backend status: <strong>{status}</strong></p>
    </div>
  )
}

export default App