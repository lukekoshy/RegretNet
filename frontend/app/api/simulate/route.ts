import { NextResponse } from "next/server";

export async function POST(req: Request) {
  try {
    const { decision } = await req.json();

    if (!decision) {
      return NextResponse.json({ error: "No decision provided" }, { status: 400 });
    }

    const apiKey = process.env.OPENROUTER_API_KEY;
    if (!apiKey) {
      return NextResponse.json({ error: "API key missing" }, { status: 500 });
    }

    const response = await fetch("https://openrouter.ai/api/v1/chat/completions", {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${apiKey}`,
        "Content-Type": "application/json",
        "HTTP-Referer": "https://regret-net-6pex.vercel.app",
        "X-Title": "RegretNet AI",
      },
      body: JSON.stringify({
        model: "meta-llama/llama-3-8b-instruct",
        messages: [
          {
            role: "system",
            content:
              "You simulate the user's future based on their decision. Provide consequences, risks, and growth opportunities.",
          },
          { role: "user", content: decision },
        ],
      }),
    });

    const data = await response.json();

    if (!data.choices) {
      console.error("OpenRouter error:", data);
      return NextResponse.json({ error: "AI failed" }, { status: 500 });
    }

    return NextResponse.json({
      future_self_message: data.choices[0].message.content,
      risks: ["Missed opportunities", "Loss of discipline"],
      growth_opportunities: ["Better habits", "Stronger mindset"],
    });
  } catch (error) {
    console.error("Server crash:", error);
    return NextResponse.json({ error: "Server error" }, { status: 500 });
  }
}
