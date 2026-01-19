"""
Growth Agent

Identifies potential long-term growth opportunities related to a decision.
"""

from services.openrouter_client import call_openrouter

def analyze_growth(decision: str) -> str:
    """
    Generates growth opportunities for a given decision.

    Args:
        decision (str): The user's decision.

    Returns:
        str: AI-generated growth opportunities.
    """

    prompt = f"""
Analyze the long-term growth opportunities of this decision:

Decision: {decision}

Return a list of potential positive outcomes for personal, career, and skill growth.
"""

    return call_openrouter(prompt)
