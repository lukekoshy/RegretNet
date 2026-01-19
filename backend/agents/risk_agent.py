"""
Risk Agent

Identifies long-term risks associated with a decision.
"""

from services.openrouter_client import call_openrouter

def analyze_risks(decision: str) -> str:
    """
    Generates risk analysis for a given decision.

    Args:
        decision (str): The user's decision.

    Returns:
        str: AI-generated list of risks.
    """

    prompt = f"""
Analyze the long-term risks of the following decision:

Decision: {decision}

Return a list of major risks.
"""

    return call_openrouter(prompt)
