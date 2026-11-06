import logging
import sys
from typing import Optional

def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Initialize and return a configured logger instance."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

class CryptoLogger:
    """Wrapper class for standardized crypto-related logging."""
    def __init__(self, name: str) -> None:
        self.logger: logging.Logger = get_logger(name)

    def info(self, msg: str, *args: object) -> None:
        """Log info level message."""
        self.logger.info(msg, *args)

    def error(self, msg: str, exc: Optional[Exception] = None) -> None:
        """Log error message with optional exception info."""
        if exc:
            self.logger.error(f"{msg}: {str(exc)}", exc_info=True)
        else:
            self.logger.error(msg)
