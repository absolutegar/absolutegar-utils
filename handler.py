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

def prepare_payload(data: Dict[str, Any]) -> Dict[str, Any]:
    timestamp = int(time.time() * 1000)
    payload = {**data, 'timestamp': timestamp}
    return payload

def validate_response_status(status_code: int) -> bool:
    return 200 <= status_code < 300

def format_crypto_price(price: float, precision: int = 8) -> str:
    return f"{price:.{precision}f}"

def sanitize_order_params(params: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in params.items() if v is not None}