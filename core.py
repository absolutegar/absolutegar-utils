import functools
from typing import Callable, Any, Dict

CACHE: Dict[tuple, Any] = {}

def memoize_crypto_calc(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (func.__name__, args, tuple(sorted(kwargs.items())))
        if key not in CACHE:
            CACHE[key] = func(*args, **kwargs)
        return CACHE[key]
    return wrapper

class CryptoProcessor:
    __slots__ = ('nonce', 'data')

    def __init__(self, nonce: int, data: bytes):
        self.nonce = nonce
        self.data = data

    @staticmethod
    @memoize_crypto_calc
    def compute_hash(val: int) -> int:
        return (val * 0x5bd1e995) & 0xffffffff

    def process(self) -> int:
        return self.compute_hash(self.nonce) ^ hash(self.data)

def batch_process(items: list[tuple[int, bytes]]) -> list[int]:
    return [CryptoProcessor(n, d).process() for n, d in items]