import functools
import time
from typing import Callable, Any, Dict

CACHE_TTL = 60
_cache: Dict[str, tuple] = {}

def memoize_crypto_data(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = f"{func.__name__}:{args}:{kwargs}"
        now = time.monotonic()
        if key in _cache:
            val, timestamp = _cache[key]
            if now - timestamp < CACHE_TTL:
                return val
        result = func(*args, **kwargs)
        _cache[key] = (result, now)
        return result
    return wrapper

class DataHandler:
    def __init__(self, engine: Any) -> None:
        self.engine = engine

    @memoize_crypto_data
    def fetch_market_state(self, pair: str) -> Dict[str, float]:
        data = self.engine.get_raw_data(pair)
        return {
            "price": float(data.get("p", 0)),
            "vol": float(data.get("v", 0)),
            "ts": time.time()
        }

    def clear_cache(self) -> None:
        _cache.clear()