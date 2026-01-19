/**
 * RegretNet AI - Premium UI
 * Futuristic, emotional, cinematic design
 */

"use client";

import { useState } from "react";

export default function Home() {
  const [decision, setDecision] = useState("");
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const submitDecision = async () => {
    if (!decision.trim()) return;

    setLoading(true);

    const res = await fetch("/api/simulate", {
      
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          decision,
          context: "User seeking long-term impact analysis",
        }),
      }
    );

    const data = await res.json();
    setResult(data);
    setLoading(false);
  };

  return (
    <main className="min-h-screen bg-gradient-to-br from-black via-purple-900 to-indigo-900 text-white flex items-center justify-center px-6">

      <div className="max-w-4xl w-full space-y-10">

        {/* HERO */}
        <div className="text-center space-y-4">
          <h1 className="text-5xl md:text-6xl font-extrabold tracking-wide">
            RegretNet AI
          </h1>
          <p className="text-purple-300 text-lg">
            See the future before you live it.
          </p>
        </div>

        {/* INPUT CARD */}
        <div className="bg-white/10 backdrop-blur-xl rounded-2xl p-6 shadow-xl space-y-4 border border-white/20">
          <textarea
            className="w-full bg-black/40 text-white rounded-xl p-4 focus:outline-none focus:ring-2 focus:ring-purple-500"
            rows={4}
            placeholder="Enter a life decision..."
            onChange={(e) => setDecision(e.target.value)}
          />

          <button
            onClick={submitDecision}
            className="w-full py-3 rounded-xl bg-purple-600 hover:bg-purple-700 transition-all font-semibold shadow-lg glow-btn"
          >

            {loading ? "Simulating your future..." : "Simulate My Future"}
          </button>
        </div>

        {/* RESULTS */}
        {result && (
          <div className="space-y-8 animate-fadeIn">

            {/* FUTURE SELF */}
            <div className="bg-white/10 backdrop-blur-xl rounded-2xl p-6 border border-white/20 shadow-xl">
              <h2 className="text-xl font-semibold text-purple-300 mb-2">
                Message from your future self
              </h2>
              <p className="text-white/90 leading-relaxed">
                {result.future_self_message}
              </p>
            </div>

            {/* RISKS */}
            <div className="grid md:grid-cols-2 gap-6">

              <div className="bg-red-500/10 border border-red-400/30 rounded-2xl p-6">
                <h3 className="text-red-400 font-semibold mb-2">Risks</h3>
                <ul className="list-disc ml-5 text-white/80">
                  {result.risks.map((r: string, i: number) => (
                    <li key={i}>{r}</li>
                  ))}
                </ul>
              </div>

              <div className="bg-green-500/10 border border-green-400/30 rounded-2xl p-6">
                <h3 className="text-green-400 font-semibold mb-2">
                  Growth Opportunities
                </h3>
                <ul className="list-disc ml-5 text-white/80">
                  {result.growth_opportunities.map((g: string, i: number) => (
                    <li key={i}>{g}</li>
                  ))}
                </ul>
              </div>

            </div>
          </div>
        )}

      </div>
    </main>
  );
}
