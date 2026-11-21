import hashlib
import hmac
import time
from typing import Dict, Any


def generate_signature(payload: str, secret: str) -> str:
    return hmac.new(
        secret.encode('utf-8'),
        payload.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()


def format_order_params(params: Dict[str, Any]) -> str:
    return '&'.join([f"{k}={v}" for k, v in sorted(params.items())])


def get_timestamp() -> str:
    return str(int(time.time() * 1000))


def validate_order_response(response: Dict[str, Any]) -> bool:
    required_fields = {'orderId', 'status', 'timestamp'}
    return all(field in response for field in required_fields)


def parse_crypto_amount(amount: float, precision: int = 8) -> str:
    return f"{amount:.{precision}f}".rstrip('0').rstrip('.')


def create_request_headers(api_key: str, signature: str) -> Dict[str, str]:
    return {
        'X-API-KEY': api_key,
        'X-SIGNATURE': signature,
        'Content-Type': 'application/json'
    }