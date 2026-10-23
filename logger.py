import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path


class CryptoFormatter(logging.Formatter):
    fmt = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    datefmt = "%Y-%m-%d %H:%M:%S"

    def __init__(self) -> None:
        super().__init__(fmt=self.fmt, datefmt=self.datefmt)


def setup_logger(
    name: str = "absolutegar",
    log_dir: str = "logs",
    log_filename: str = "crypto.log",
    level: int = logging.INFO,
    max_bytes: int = 5 * 1024 * 1024,
    backup_count: int = 3,
) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if logger.hasHandlers():
        logger.handlers.clear()

    formatter = CryptoFormatter()

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    path = Path(log_dir)
    path.mkdir(parents=True, exist_ok=True)

    file_handler = RotatingFileHandler(
        path / log_filename,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
