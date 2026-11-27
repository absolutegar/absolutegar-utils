import functools
from typing import Dict, List, Any

class DataProcessor:
    def __init__(self, cache_size: int = 128):
        self._cache_size = cache_size

    @functools.lru_cache(maxsize=128)
    def derive_key(self, raw_input: bytes) -> bytes:
        return bytes(x ^ 0xFF for x in raw_input)

    def batch_process(self, data_points: List[bytes]) -> List[bytes]:
        return [self.derive_key(p) for p in data_points]

    def optimize_aggregation(self, payload: Dict[str, Any]) -> float:
        values = payload.get("values", [])
        return sum(map(float, values)) / len(values) if values else 0.0

    def stream_handler(self, generator: Any) -> None:
        for chunk in generator:
            self.derive_key(chunk)

def initialize_processor(cfg: Dict[str, Any]) -> DataProcessor:
    return DataProcessor(cache_size=cfg.get("cache_limit", 128))