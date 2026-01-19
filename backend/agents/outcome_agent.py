"""
Outcome Agent

Simulates best, worst, and realistic future timelines for a given decision.
"""

from services.openrouter_client import call_openrouter

def generate_outcomes(decision: str, context: str | None) -> str:
    """
    Generates future timeline outcomes using the AI model.

    Args:
        decision (str): The user's decision.
        context (str | None): Optional background context.

    Returns:
        str: Raw AI-generated text describing future outcomes.
    """

    prompt = f"""
You are a future simulation AI.

Decision: {decision}
Context: {context or "None"}

Generate three futures:
1. Best case
2. Worst case
3. Realistic case

Each must include:
- Summary
- Career impact
- Health impact
- Financial impact
- Social impact
"""

    return call_openrouter(prompt)
