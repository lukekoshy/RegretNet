"""
Logging Configuration

Sets up application-wide logging for debugging and monitoring.
"""

import logging

def setup_logger():
    """
    Configures logging format and level.
    """

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )
