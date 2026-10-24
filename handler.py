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

def format_payload(params: Dict[str, Any]) -> str:
    sorted_keys = sorted(params.keys())
    return '&'.join([f"{k}={params[k]}" for k in sorted_keys])

def sign_request(api_secret: str, params: Dict[str, Any]) -> Dict[str, Any]:
    params['timestamp'] = int(time.time() * 1000)
    query_string = format_payload(params)
    params['signature'] = generate_signature(api_secret, query_string)
    return params

def validate_order_data(data: Dict[str, Any]) -> bool:
    required = {'symbol', 'side', 'type', 'quantity'}
    return all(key in data for key in required)