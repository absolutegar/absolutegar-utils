import hashlib
import hmac
import time
import json
from typing import Dict, Any

def generate_signature(api_secret: str, message: str) -> str:
    return hmac.new(
        api_secret.encode('utf-8'),
        message.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def format_payload(params: Dict[str, Any]) -> str:
    return json.dumps(dict(sorted(params.items())))

def get_timestamp() -> int:
    return int(time.time() * 1000)

def parse_order_response(response: Dict[str, Any]) -> Dict[str, Any]:
    return {
        'id': response.get('order_id'),
        'status': response.get('status'),
        'filled': float(response.get('filled_qty', 0)),
        'price': float(response.get('avg_price', 0))
    }

def validate_ticker(symbol: str) -> bool:
    if not isinstance(symbol, str) or len(symbol) < 3:
        return False
    return symbol.isalnum()