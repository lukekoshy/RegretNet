"""
Retry Utility

Provides a simple retry mechanism for unreliable external calls.
"""

import time
import logging

logger = logging.getLogger(__name__)

def retry(func, retries=3, delay=2):
    """
    Retries a function call on failure.

    Args:
        func (callable): Function to retry.
        retries (int): Number of attempts.
        delay (int): Delay between attempts.

    Returns:
        Any: Function result or fallback message.
    """

    for attempt in range(retries):
        try:
            return func()
        except Exception as e:
            logger.warning(f"Retry {attempt + 1} failed: {str(e)}")
            time.sleep(delay)

    return "Fallback: AI service temporarily unavailable."
