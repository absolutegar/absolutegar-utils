import hashlib
import hmac
import time
from typing import Dict, Any

def generate_signature(api_secret: str, message: str) -> str:
    return hmac.new(
        api_secret.encode('utf-8'),
        message.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def get_timestamp() -> int:
    return int(time.time() * 1000)

def sanitize_params(params: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in params.items() if v is not None}

class CryptoFormatter:
    @staticmethod
    def format_amount(amount: float, precision: int = 8) -> str:
        return f"{amount:.{precision}f}"

    @staticmethod
    def validate_pair(pair: str) -> bool:
        return isinstance(pair, str) and "_" in pair