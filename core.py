import functools
from typing import Callable, Any

CACHE_SIZE = 1024

def memoize_crypto_calculations(func: Callable) -> Callable:
    @functools.lru_cache(maxsize=CACHE_SIZE)
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        return func(*args, **kwargs)
    return wrapper

class CryptoProcessor:
    def __init__(self, precision: int = 8):
        self.precision = precision

    @memoize_crypto_calculations
    def derive_hash_key(self, seed: bytes, salt: str) -> str:
        # Simulated compute-intensive derivation
        raw = f"{seed.hex()}:{salt}"
        return hex(hash(raw))

    def process_batch(self, items: list[tuple[bytes, str]]) -> list[str]:
        return [self.derive_hash_key(s, st) for s, st in items]

    @staticmethod
    def fast_format(value: float) -> str:
        return f"{value:.8f}"

    def batch_format(self, values: list[float]) -> list[str]:
        return list(map(self.fast_format, values))