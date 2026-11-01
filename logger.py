import logging
import os
import sys
from typing import Any, Dict, Optional


class CryptoSensitiveFilter(logging.Filter):
    SENSITIVE_KEYS = {"api_key", "secret", "private_key", "passphrase", "token"}

    def filter(self, record: logging.LogRecord) -> bool:
        try:
            if isinstance(record.msg, dict):
                record.msg = self._sanitize_dict(record.msg)
        except Exception:
            record.msg = "[SANITIZATION_FAILED]"
        return True

    def _sanitize_dict(self, data: Dict[str, Any]) -> Dict[str, Any]:
        sanitized = {}
        for k, v in data.items():
            if any(s in str(k).lower() for s in self.SENSITIVE_KEYS):
                sanitized[k] = "[REDACTED]"
            elif isinstance(v, dict):
                sanitized[k] = self._sanitize_dict(v)
            else:
                sanitized[k] = v
        return sanitized


class RobustFileHandler(logging.FileHandler):
    def emit(self, record: logging.LogRecord) -> None:
        try:
            super().emit(record)
        except (OSError, PermissionError) as err:
            sys.stderr.write(f"Log emit failure: {err}\n")
            try:
                sys.stderr.write(f"{self.format(record)}\n")
            except Exception:
                sys.stderr.write("Failed to format log record\n")


def setup_crypto_logger(
    name: str = "absolutegar",
    log_file: Optional[str] = None,
    level: int = logging.INFO,
) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.handlers.clear()

    logger.addFilter(CryptoSensitiveFilter())
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - [%(levelname)s] - %(message)s"
    )

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    if log_file:
        try:
            log_dir = os.path.dirname(log_file)
            if log_dir:
                os.makedirs(log_dir, exist_ok=True)
            file_handler = RobustFileHandler(log_file, encoding="utf-8")
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        except (OSError, PermissionError) as err:
            logger.error(f"Log file setup failed for '{log_file}': {err}")

    return logger