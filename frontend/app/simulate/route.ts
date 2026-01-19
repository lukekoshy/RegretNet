import { NextResponse } from "next/server";

export async function POST(req: Request) {
  const body = await req.json();

  const decision = body.decision;

  const response = await fetch("https://openrouter.ai/api/v1/chat/completions", {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${process.env.OPENROUTER_API_KEY}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      model: "mistralai/mistral-7b-instruct",
      messages: [
        {
          role: "user",
          content: `You are the user's future self. Reflect on this decision:\n\n${decision}`,
        },
      ],
    }),
  });

  const data = await response.json();

  return NextResponse.json({
    future_self_message: data.choices[0].message.content,
    risks: ["Missed fitness goals", "Lower energy"],
    growth_opportunities: ["Better discipline", "Improved focus"],
  });
}
