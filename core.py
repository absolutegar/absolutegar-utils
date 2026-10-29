import hashlib
import hmac
import time
from typing import Any, Dict

def generate_signature(api_secret: str, payload: str) -> str:
    return hmac.new(
        api_secret.encode('utf-8'),
        payload.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def format_payload(params: Dict[str, Any]) -> str:
    sorted_keys = sorted(params.keys())
    return '&'.join([f'{k}={params[k]}' for k in sorted_keys])

def get_timestamp() -> int:
    return int(time.time() * 1000)

def validate_order_params(params: Dict[str, Any]) -> bool:
    required = ['symbol', 'side', 'type', 'quantity']
    return all(key in params for key in required)

def sanitize_currency(pair: str) -> str:
    return pair.upper().replace('/', '_')

def build_request_headers(api_key: str, signature: str) -> Dict[str, str]:
    return {
        'X-API-KEY': api_key,
        'X-SIGNATURE': signature,
        'Content-Type': 'application/json'
    }