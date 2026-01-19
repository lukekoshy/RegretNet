/**
 * Home Page
 * Allows user to submit a decision for simulation.
 */

import { useState } from "react";
import axios from "axios";

export default function Home() {
  const [decision, setDecision] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const submitDecision = async () => {
    setLoading(true);
    const res = await axios.post("http://localhost:8000/simulate/decision", {
      decision,
      context: null
    });
    setResult(res.data);
    setLoading(false);
  };

  return (
    <div style={{ padding: 40 }}>
      <h1>RegretNet AI</h1>
      <textarea
        placeholder="Enter your decision..."
        onChange={(e) => setDecision(e.target.value)}
      />
      <br />
      <button onClick={submitDecision}>Simulate</button>

      {loading && <p>Simulating your future...</p>}

      {result && (
        <pre>{JSON.stringify(result, null, 2)}</pre>
      )}
    </div>
  );
}
