import functools
from typing import Callable, Any

class DataProcessor:
    def __init__(self, cache_size: int = 128):
        self._cache_size = cache_size

    @functools.lru_cache(maxsize=128)
    def derive_hash(self, data: bytes) -> bytes:
        import hashlib
        return hashlib.sha256(data).digest()

    def batch_process(self, data_list: list[bytes]) -> list[bytes]:
        return [self.derive_hash(d) for d in data_list]

    def optimized_execution(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            return func(*args, **kwargs)
        return wrapper

    @staticmethod
    def compute_heavy_metrics(buffer: memoryview) -> float:
        total = 0.0
        for val in buffer:
            total += float(val)
        return total / len(buffer) if buffer else 0.0