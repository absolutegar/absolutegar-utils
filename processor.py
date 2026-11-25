from dataclasses import dataclass
from typing import Dict, List


@dataclass(slots=True)
class Tick:
    timestamp: float
    price: float
    volume: float


@dataclass(slots=True)
class Candle:
    timestamp: int
    open: float
    high: float
    low: float
    close: float
    volume: float


class BatchProcessor:
    def __init__(self, interval_seconds: int = 60) -> None:
        self.interval = interval_seconds
        self._buffers: Dict[str, List[Tick]] = {}

    def add_tick(self, symbol: str, timestamp: float, price: float, volume: float) -> None:
        if symbol not in self._buffers:
            self._buffers[symbol] = []
        self._buffers[symbol].append(Tick(timestamp, price, volume))

    def process_symbol(self, symbol: str) -> List[Candle]:
        ticks = self._buffers.get(symbol, [])
        if not ticks:
            return []

        ticks.sort(key=lambda t: t.timestamp)
        candles: List[Candle] = []
        current_bucket: int | None = None
        c_open = c_high = c_low = c_close = c_vol = 0.0

        for tick in ticks:
            bucket = int(tick.timestamp // self.interval) * self.interval
            if current_bucket is None:
                current_bucket = bucket
                c_open = c_high = c_low = c_close = tick.price
                c_vol = tick.volume
            elif bucket == current_bucket:
                if tick.price > c_high:
                    c_high = tick.price
                elif tick.price < c_low:
                    c_low = tick.price
                c_close = tick.price
                c_vol += tick.volume
            else:
                candles.append(Candle(current_bucket, c_open, c_high, c_low, c_close, c_vol))
                current_bucket = bucket
                c_open = c_high = c_low = c_close = tick.price
                c_vol = tick.volume

        if current_bucket is not None:
            candles.append(Candle(current_bucket, c_open, c_high, c_low, c_close, c_vol))

        self._buffers[symbol].clear()
        return candles

    def clear(self) -> None:
        self._buffers.clear()
