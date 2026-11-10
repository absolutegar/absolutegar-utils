import hashlib
import hmac
from decimal import Decimal, ROUND_DOWN
from typing import Any, Dict, Union


class CryptoProcessor:

    @staticmethod
    def to_wei(amount: Union[int, float, str, Decimal], decimals: int = 18) -> int:
        val = Decimal(str(amount))
        return int(val * (Decimal(10) ** decimals))

    @staticmethod
    def from_wei(amount: int, decimals: int = 18) -> Decimal:
        val = Decimal(str(amount))
        return val / (Decimal(10) ** decimals)

    @staticmethod
    def generate_signature(secret: str, payload: str) -> str:
        return hmac.new(
            secret.encode("utf-8"),
            payload.encode("utf-8"),
            hashlib.sha256,
        ).hexdigest()

    @staticmethod
    def parse_trade_payload(raw_data: Dict[str, Any]) -> Dict[str, Any]:
        symbol = str(raw_data.get("symbol", "")).upper()
        price = Decimal(str(raw_data.get("price", "0")))
        quantity = Decimal(str(raw_data.get("quantity", "0")))
        total = (price * quantity).quantize(Decimal("0.00000001"), rounding=ROUND_DOWN)

        return {
            "symbol": symbol,
            "price": price,
            "quantity": quantity,
            "total": total,
            "timestamp": raw_data.get("timestamp"),
        }
