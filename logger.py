import logging
import sys
from typing import Optional

class AbsoluteLogger:
    def __init__(self, name: str = "absolutegar", level: int = logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.logger.propagate = False
        self._setup_handlers()

    def _setup_handlers(self) -> None:
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setFormatter(formatter)
        self.logger.addHandler(stdout_handler)

    def get_logger(self) -> logging.Logger:
        return self.logger

def get_default_logger(name: str = "absolutegar") -> logging.Logger:
    return AbsoluteLogger(name).get_logger()