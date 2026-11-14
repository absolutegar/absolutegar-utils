import hashlib
import hmac
from typing import Dict, Any


def generate_signature(api_secret: str, payload: str) -> str:
    return hmac.new(
        api_secret.encode('utf-8'),
        payload.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()


def format_order_params(params: Dict[str, Any]) -> str:
    return '&'.join(f"{k}={v}" for k, v in sorted(params.items()))


def parse_crypto_amount(amount: str) -> float:
    try:
        return float(amount)
    except ValueError:
        return 0.0


def validate_ticker(ticker: str) -> bool:
    if not isinstance(ticker, str) or len(ticker) < 2:
        return False
    return ticker.isalnum()


def sanitize_response(data: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in data.items() if v is not None}