import logging
from logging.handlers import RotatingFileHandler

from ai_contact_hub.config import LOG_FILE



def setup_logging():
    LOG_FILE.parent.mkdir(exist_ok=True)
    logger = logging.getLogger("requests")
    if logger.handlers:
        return
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=5_000_000,
        backupCount=3,
    )
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
