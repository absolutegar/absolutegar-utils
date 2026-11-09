from typing import Any, Dict, List, Optional


class TickProcessor:
    def __init__(self, interval_seconds: int = 60) -> None:
        self.interval = interval_seconds

    def parse_tick(self, payload: Dict[str, Any]) -> Optional[Dict[str, float]]:
        price = payload.get("price") or payload.get("p")
        volume = payload.get("quantity") or payload.get("q") or payload.get("amount")
        timestamp = payload.get("timestamp") or payload.get("t")

        if price is None or volume is None or timestamp is None:
            return None

        return {
            "price": float(price),
            "volume": float(volume),
            "timestamp": float(timestamp),
        }

    def aggregate_ohlcv(self, ticks: List[Dict[str, Any]]) -> List[Dict[str, float]]:
        parsed_ticks = []
        for tick in ticks:
            parsed = self.parse_tick(tick)
            if parsed:
                parsed_ticks.append(parsed)

        if not parsed_ticks:
            return []

        parsed_ticks.sort(key=lambda x: x["timestamp"])

        candles: List[Dict[str, float]] = []
        current_candle: Optional[Dict[str, float]] = None
        bucket_start = 0.0

        for tick in parsed_ticks:
            ts = tick["timestamp"]
            price = tick["price"]
            vol = tick["volume"]
            tick_bucket = (ts // self.interval) * self.interval

            if current_candle is None or tick_bucket != bucket_start:
                if current_candle:
                    candles.append(current_candle)
                bucket_start = tick_bucket
                current_candle = {
                    "timestamp": bucket_start,
                    "open": price,
                    "high": price,
                    "low": price,
                    "close": price,
                    "volume": vol,
                }
            else:
                current_candle["high"] = max(current_candle["high"], price)
                current_candle["low"] = min(current_candle["low"], price)
                current_candle["close"] = price
                current_candle["volume"] += vol

        if current_candle:
            candles.append(current_candle)

        return candles
