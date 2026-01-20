import { NextResponse } from "next/server";

export async function POST(req: Request) {
  try {
    const { decision } = await req.json();

    if (!decision) {
      return NextResponse.json(
        { error: "No decision provided" },
        { status: 400 }
      );
    }

    const apiKey = process.env.OPENROUTER_API_KEY;

    if (!apiKey) {
      console.error("Missing API key");
      return NextResponse.json(
        { error: "API key missing" },
        { status: 500 }
      );
    }

    const response = await fetch(
      "https://openrouter.ai/api/v1/chat/completions",
      {
        method: "POST",
        headers: {
          Authorization: `Bearer ${apiKey}`,
          "Content-Type": "application/json",
          "HTTP-Referer": "https://regretnet.onrender.com",
          "X-Title": "RegretNet AI",
        },
        body: JSON.stringify({
          model: "mistralai/mistral-7b-instruct",
          messages: [
            {
              role: "system",
              content:
                "You simulate the user's future based on their decision. Give a realistic message, risks, and growth opportunities.",
            },
            { role: "user", content: decision },
          ],
          max_tokens: 300,
        }),
      }
    );

    const data = await response.json();

    if (!data.choices || !data.choices[0]) {
      console.error("OpenRouter error:", data);
      return NextResponse.json(
        {
          future_self_message: "AI service temporarily unavailable.",
          risks: ["Service instability"],
          growth_opportunities: ["Try again later"],
        },
        { status: 200 }
      );
    }

    const message = data.choices[0].message.content;

    return NextResponse.json({
      future_self_message: message,
      risks: [
        "Short-term comfort",
        "Missed long-term discipline",
      ],
      growth_opportunities: [
        "Consistency",
        "Stronger future self",
      ],
    });
  } catch (err) {
    console.error("Server error:", err);
    return NextResponse.json(
      {
        future_self_message: "Unable to process your decision at this time.",
        risks: ["Processing error"],
        growth_opportunities: ["Please try again"],
      },
      { status: 200 }
    );
  }
}
