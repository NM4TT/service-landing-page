import logging
import os

logging_level_str = os.getenv("LOGGING_LEVEL", "INFO").upper()

log_level = getattr(logging, logging_level_str, logging.INFO)

logging.basicConfig(
    level=log_level,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    #filename="/logs/myserver.log",
    filemode="a"
)

def get_logger(name: str = None):
    return logging.getLogger(name)