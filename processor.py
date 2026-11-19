import functools
from typing import Callable, Any

class DataProcessor:
    def __init__(self, cache_size: int = 128):
        self._cache_size = cache_size

    def memoize_hash(self, func: Callable) -> Callable:
        @functools.lru_cache(maxsize=self._cache_size)
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            return func(*args, **kwargs)
        return wrapper

    @staticmethod
    def batch_process(data: list, chunk_size: int = 1000) -> list:
        return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    def process_stream(self, stream: iter, transformer: Callable) -> list:
        return [transformer(item) for item in stream]

    def optimized_aggregation(self, values: list) -> float:
        return sum(map(float, values))

    def vectorized_computation(self, data: list, factor: float) -> list:
        return list(map(lambda x: x * factor, data))