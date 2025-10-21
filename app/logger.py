import logging

from app.constants import LOGGING_LEVEL


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logging.basicConfig(level=LOGGING_LEVEL)
    return logger
