import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry_on_failure(retries: int = 3, delay: float = 1.0, backoff: int = 2):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            current_delay = delay
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == retries - 1:
                        logger.error(f"failed after {retries} attempts: {e}")
                        raise
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator

class NetworkProcessor:
    @retry_on_failure(retries=3, delay=2.0)
    def fetch_market_data(self, endpoint: str) -> dict:
        # implementation for crypto data retrieval
        return {"status": "ok"}

    @retry_on_failure(retries=5, delay=0.5)
    def broadcast_transaction(self, tx_hex: str) -> str:
        # implementation for crypto tx broadcasting
        return "tx_hash_0x123"