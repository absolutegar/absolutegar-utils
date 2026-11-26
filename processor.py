import json
from typing import Any, Dict, List
from decimal import Decimal, ROUND_HALF_UP

class CryptoDataProcessor:
    @staticmethod
    def format_balance(amount: str, precision: int = 8) -> str:
        return str(Decimal(amount).quantize(Decimal('1.' + '0' * precision), rounding=ROUND_HALF_UP))

    @staticmethod
    def sanitize_orderbook(data: Dict[str, Any]) -> Dict[str, List[List[str]]]:
        sanitized = {"bids": [], "asks": []}
        for side in ["bids", "asks"]:
            if side in data:
                sanitized[side] = [[str(p), str(a)] for p, a in data[side]]
        return sanitized

    @staticmethod
    def calculate_mid_price(bid: str, ask: str) -> Decimal:
        return (Decimal(bid) + Decimal(ask)) / Decimal('2')

    @staticmethod
    def validate_payload(data: Any) -> bool:
        try:
            json.dumps(data)
            return isinstance(data, (dict, list))
        except (TypeError, ValueError):
            return False

    @classmethod
    def process_ticker(cls, ticker: Dict[str, Any]) -> Dict[str, str]:
        return {
            "symbol": str(ticker.get("symbol", "UNKNOWN")),
            "price": cls.format_balance(str(ticker.get("price", "0"))),
            "volume": cls.format_balance(str(ticker.get("volume", "0")))
        }