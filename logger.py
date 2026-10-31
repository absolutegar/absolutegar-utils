import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


def setup_logger(
    name: str = "absolutegar",
    log_dir: str = "logs",
    log_file: str = "crypto_utils.log",
    level: int = logging.INFO,
    max_bytes: int = 10_485_760,
    backup_count: int = 5,
) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    log_path = Path(log_dir)
    log_path.mkdir(parents=True, exist_ok=True)
    file_path = log_path / log_file

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    file_handler = RotatingFileHandler(
        file_path,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger


def get_logger(name: str = "absolutegar") -> logging.Logger:
    return logging.getLogger(name)
