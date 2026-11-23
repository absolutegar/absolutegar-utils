from functools import lru_cache
from typing import List, Dict, Any
import math

class DataProcessor:
    def __init__(self, precision: int = 8):
        self.precision = precision
        self.factor = 10**precision

    @lru_cache(maxsize=1024)
    def normalize_value(self, value: float) -> int:
        return int(math.floor(value * self.factor))

    def process_batch(self, data: List[Dict[str, float]]) -> List[Dict[str, int]]:
        return [
            {
                "id": item["id"],
                "val": self.normalize_value(item["price"])
            }
            for item in data
        ]

    def calculate_weighted_average(self, values: List[float], weights: List[float]) -> float:
        if len(values) != len(weights):
            raise ValueError("mismatch in sequence lengths")
        
        total_weight = sum(weights)
        if total_weight == 0:
            return 0.0
            
        return sum(v * w for v, w in zip(values, weights)) / total_weight