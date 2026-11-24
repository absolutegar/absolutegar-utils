import hashlib
import hmac
from functools import lru_cache
from typing import Dict, Any

@lru_cache(maxsize=1024)
def compute_signature(secret: str, message: str) -> str:
    return hmac.new(
        secret.encode(),
        message.encode(),
        hashlib.sha256
    ).hexdigest()

def batch_process_signatures(secret: str, payloads: tuple) -> list:
    return [compute_signature(secret, p) for p in payloads]

class CacheProcessor:
    def __init__(self, data: Dict[str, Any]):
        self._data = data

    def get_optimized_value(self, key: str) -> Any:
        return self._data.get(key)

    @staticmethod
    def fast_hash(data: str) -> int:
        return hash(data) & 0xffffffff

def clean_nones(d: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in d.items() if v is not None}