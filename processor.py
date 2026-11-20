import hashlib
from typing import List, Dict, Any

class DataProcessor:
    def __init__(self, salt: str = "absolutegar"):
        self.salt = salt

    def sanitize(self, data: Dict[str, Any]) -> Dict[str, Any]:
        return {k: str(v).strip() for k, v in data.items() if v is not None}

    def compute_hash(self, payload: str) -> str:
        return hashlib.sha256(f"{payload}{self.salt}".encode()).hexdigest()

    def process_batch(self, items: List[Dict[str, Any]]) -> List[str]:
        sanitized = [self.sanitize(i) for i in items]
        return [self.compute_hash(str(item.values())) for item in sanitized]

    @staticmethod
    def validate_keys(data: Dict[str, Any], required: List[str]) -> bool:
        return all(key in data for key in required)