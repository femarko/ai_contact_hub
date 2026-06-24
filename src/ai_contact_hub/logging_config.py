import logging
from logging.handlers import RotatingFileHandler

from ai_contact_hub.config import LOG_FILE



def setup_logging():
    LOG_FILE.parent.mkdir(exist_ok=True)

    handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=5_000_000,
        backupCount=3,
    )

    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(message)s"
    )

    handler.setFormatter(formatter)

    for logger_name in ["requests", "ai", "emails"]:
        logger = logging.getLogger(logger_name)
        if logger.handlers:
            continue
        logger.setLevel(logging.INFO)
        logger.propagate = False
        logger.addHandler(handler)
