import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

def get_logger(name: str, log_file: str = "absolutegar.log") -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        log_path = Path(log_file)
        handler = RotatingFileHandler(
            log_path,
            maxBytes=10 * 1024 * 1024,
            backupCount=5,
            encoding="utf-8"
        )
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)

    return logger