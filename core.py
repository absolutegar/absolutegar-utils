import hashlib
import hmac
from collections import deque
from functools import lru_cache
from typing import List, Tuple


class FastCryptoEngine:
    def __init__(self, secret: str, max_cache_size: int = 1024):
        self.secret = secret.encode("utf-8")
        self._buffer: deque = deque(maxlen=max_cache_size)

    @lru_cache(maxsize=4096)
    def generate_signature(self, payload: str) -> str:
        return hmac.new(
            self.secret, payload.encode("utf-8"), hashlib.sha256
        ).hexdigest()

    def verify_signature(self, payload: str, signature: str) -> bool:
        expected = self.generate_signature(payload)
        return hmac.compare_digest(expected, signature)

    def batch_verify(self, items: List[Tuple[str, str]]) -> List[bool]:
        return [self.verify_signature(p, sig) for p, sig in items]

    def push_ticker_delta(self, price: float, volume: float) -> None:
        self._buffer.append((price, volume))

    def calculate_vwap(self) -> float:
        if not self._buffer:
            return 0.0
        total_pv = sum(price * vol for price, vol in self._buffer)
        total_vol = sum(vol for _, vol in self._buffer)
        return total_pv / total_vol if total_vol > 0 else 0.0

    def clear_cache(self) -> None:
        self.generate_signature.cache_clear()
