import { NextResponse } from "next/server";

export async function POST(req: Request) {
  try {
    const { decision, context } = await req.json();

    if (!decision) {
      return NextResponse.json({ error: "No decision provided" }, { status: 400 });
    }

    const apiKey = process.env.OPENROUTER_API_KEY;
    if (!apiKey) {
      return NextResponse.json({ error: "API key not configured" }, { status: 500 });
    }

    // Call OpenRouter API
    const response = await fetch("https://openrouter.ai/api/v1/chat/completions", {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${apiKey}`,
        "Content-Type": "application/json",
        "HTTP-Referer": "https://regretnet.vercel.app",
        "X-Title": "RegretNet AI",
      },
      body: JSON.stringify({
        model: "meta-llama/llama-3-8b-instruct",
        messages: [
          {
            role: "system",
            content: "You are a future simulation AI that analyzes decisions. Provide a detailed response covering: future self message, risks, and growth opportunities.",
          },
          {
            role: "user",
            content: `Decision: ${decision}\nContext: ${context || "None"}`
          },
        ],
      }),
    });

    const data = await response.json();

    if (!data.choices || !data.choices[0]?.message?.content) {
      console.error("OpenRouter response:", data);
      return NextResponse.json({
        future_self_message: "Unable to process your decision at this time.",
        risks: ["Processing error"],
        growth_opportunities: ["Please try again"],
      });
    }

    const aiResponse = data.choices[0].message.content;

    return NextResponse.json({
      future_self_message: aiResponse,
      risks: ["Potential risk identified", "Consider outcomes carefully"],
      growth_opportunities: ["Personal development opportunity", "Increased self-awareness"],
    });

  } catch (error) {
    console.error("Simulation error:", error);
    return NextResponse.json({
      future_self_message: "Error processing your decision.",
      risks: ["System error"],
      growth_opportunities: [],
    }, { status: 500 });
  }
}
