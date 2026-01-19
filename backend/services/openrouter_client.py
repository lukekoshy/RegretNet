"""
Client for communicating with OpenRouter's API.

Handles:
- Authorization
- Request formatting
- Response parsing
"""

import requests
from config import OPENROUTER_API_KEY, OPENROUTER_BASE_URL

def call_openrouter(prompt: str) -> str:
    """
    Sends a prompt to OpenRouter and returns the model response.

    Args:
        prompt (str): The prompt to send.

    Returns:
        str: The generated response text.
    """

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(
        f"{OPENROUTER_BASE_URL}/chat/completions",
        headers=headers,
        json=payload,
        timeout=30
    )

    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]
