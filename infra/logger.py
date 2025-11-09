import logging
import sys
from infra.config import settings


def setup_logging():

    # Getting log_level from DEBUG setting
    log_level = logging.DEBUG if settings.DEBUG else logging.INFO

    # Creating root logger
    logger = logging.getLogger()
    logger.setLevel(log_level)

    # Clearing old handlers
    if logger.hasHandlers():
        logger.handlers.clear()

    # Creating console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(log_level)

    # Formatting
    formatter = logging.Formatter(
        fmt="{asctime} | {levelname} | {name} | {message}",
        datefmt="%Y-%m-%d %H:%M:%S",
        style="{"
    )
    console_handler.setFormatter(formatter)

    # Adding handler to logger
    logger.addHandler(console_handler)

    logger.debug('Logging is configured. Log level: %s',
                 logging.getLevelName(log_level))
