import logging

logger = logging.getLogger("weather-tracker")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

handler.setFormatter(formatter)

if not logger.handlers:
    logger.addHandler(handler)


def log_info(message: str):
    logger.info(message)


def log_error(message: str):
    logger.error(message)
