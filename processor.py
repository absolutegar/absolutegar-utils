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

def normalize_order_params(params: Dict[str, Any]) -> str:
    keys = sorted(params.keys())
    return '&'.join([f"{k}={params[k]}" for k in keys])

def get_timestamp_ms() -> int:
    return int(time.time() * 1000)

def sanitize_float(value: float, precision: int = 8) -> float:
    return round(float(value), precision)

def validate_response_status(data: Dict[str, Any]) -> bool:
    if not data or 'code' not in data:
        return False
    return int(data['code']) == 200