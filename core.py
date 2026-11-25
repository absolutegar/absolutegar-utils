import hashlib
import hmac
from typing import Dict, List, Tuple


class FastOrderBook:
    __slots__ = ("_bids", "_asks", "_bid_cache", "_ask_cache")

    def __init__(self) -> None:
        self._bids: Dict[float, float] = {}
        self._asks: Dict[float, float] = {}
        self._bid_cache: List[Tuple[float, float]] = []
        self._ask_cache: List[Tuple[float, float]] = []

    def update_depth(
        self, bids: List[Tuple[float, float]], asks: List[Tuple[float, float]]
    ) -> None:
        for price, qty in bids:
            if qty == 0.0:
                self._bids.pop(price, None)
            else:
                self._bids[price] = qty

        for price, qty in asks:
            if qty == 0.0:
                self._asks.pop(price, None)
            else:
                self._asks[price] = qty

        self._bid_cache.clear()
        self._ask_cache.clear()

    def get_top_bids(self, depth: int = 10) -> List[Tuple[float, float]]:
        if not self._bid_cache:
            self._bid_cache = sorted(
                self._bids.items(), key=lambda x: x[0], reverse=True
            )
        return self._bid_cache[:depth]

    def get_top_asks(self, depth: int = 10) -> List[Tuple[float, float]]:
        if not self._ask_cache:
            self._ask_cache = sorted(self._asks.items(), key=lambda x: x[0])
        return self._ask_cache[:depth]

    def calculate_vwap(self, depth: int = 5) -> Tuple[float, float]:
        bids = self.get_top_bids(depth)
        asks = self.get_top_asks(depth)

        bid_vol = sum(q for _, q in bids)
        ask_vol = sum(q for _, q in asks)

        bid_vwap = sum(p * q for p, q in bids) / bid_vol if bid_vol else 0.0
        ask_vwap = sum(p * q for p, q in asks) / ask_vol if ask_vol else 0.0

        return bid_vwap, ask_vwap


def fast_hmac_sha256(secret: bytes, message: bytes) -> str:
    return hmac.new(secret, message, hashlib.sha256).hexdigest()
