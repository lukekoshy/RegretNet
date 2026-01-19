"""
Future Self Agent

Generates a narrative message from the user's future self.
"""

from services.openrouter_client import call_openrouter

def generate_future_message(decision: str) -> str:
    """
    Generates a message written from the perspective of the user's future self.

    Args:
        decision (str): The user's decision.

    Returns:
        str: AI-generated future-self narrative.
    """

    prompt = f"""
You are the user's future self, 5 years from now.

Reflect on this past decision:

Decision: {decision}

Write a personal letter describing how this decision affected your life.
"""

    return call_openrouter(prompt)
