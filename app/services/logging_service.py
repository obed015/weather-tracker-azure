import logging
import json
from typing import Optional, Dict, Any

# Create named logger
logger = logging.getLogger("weather-tracker")

# Set global log level
logger.setLevel(logging.INFO)

# Create console handler
handler = logging.StreamHandler()

# Structured log format
formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

handler.setFormatter(formatter)

# Prevent duplicate handlers
if not logger.handlers:
    logger.addHandler(handler)


# Structured logging helpers

def log_info(
    message: str,
    context: Optional[Dict[str, Any]] = None
):
    """
    Log informational events.

    Example:
        log_info(
            "Weather request started",
            {"city": "London"}
        )
    """

    if context:
        message = f"{message} | {json.dumps(context)}"

    logger.info(message)


def log_error(
    message: str,
    context: Optional[Dict[str, Any]] = None
):
    """
    Log error events.

    Example:
        log_error(
            "Weather request failed",
            {"city": "London", "error": "timeout"}
        )
    """

    if context:
        message = f"{message} | {json.dumps(context)}"

    logger.error(message)


def log_warning(
    message: str,
    context: Optional[Dict[str, Any]] = None
):
    """
    Log warning events.
    """

    if context:
        message = f"{message} | {json.dumps(context)}"

    logger.warning(message)
