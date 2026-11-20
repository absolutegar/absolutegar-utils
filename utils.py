import hashlib
import hmac
import time
from typing import Any, Dict, Optional


class CryptoUtils:
    @staticmethod
    def generate_signature(api_secret: str, message: str) -> str:
        return hmac.new(
            api_secret.encode('utf-8'),
            message.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()

    @staticmethod
    def format_order_params(params: Dict[str, Any]) -> str:
        sorted_keys = sorted(params.keys())
        return '&'.join([f"{k}={params[k]}" for k in sorted_keys])

    @staticmethod
    def get_timestamp() -> int:
        return int(time.time() * 1000)

    @staticmethod
    def validate_price_precision(price: float, tick_size: float) -> bool:
        if tick_size <= 0:
            return False
        return (price / tick_size).is_integer()


def calculate_account_leverage(margin: float, balance: float) -> float:
    if balance == 0:
        return 0.0
    return round(margin / balance, 4)