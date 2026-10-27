import logging
import sys
from typing import Optional

class AbsoluteLogger:
    """Standardized logger for absolutegar-utils."""
    def __init__(self, name: str, level: int = logging.INFO) -> None:
        self.logger: logging.Logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self._setup_handler()

    def _setup_handler(self) -> None:
        """Configure stream handler with basic formatting."""
        handler: logging.StreamHandler = logging.StreamHandler(sys.stdout)
        formatter: logging.Formatter = logging.Formatter(
            "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def get_logger(self) -> logging.Logger:
        """Return the configured logger instance."""
        return self.logger

def get_module_logger(name: str, level: Optional[int] = None) -> logging.Logger:
    """Factory function for consistent module logging."""
    log_level: int = level or logging.INFO
    return AbsoluteLogger(name, log_level).get_logger()