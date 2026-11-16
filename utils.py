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


def format_order_payload(symbol: str, side: str, amount: float, price: float) -> Dict[str, Any]:
    return {
        'symbol': symbol.upper(),
        'side': side.lower(),
        'quantity': str(amount),
        'price': str(price),
        'timestamp': int(time.time() * 1000)
    }


def validate_ticker(ticker: str) -> bool:
    if not isinstance(ticker, str) or len(ticker) < 2:
        return False
    return ticker.isalnum()


def parse_raw_response(data: Dict[str, Any]) -> Dict[str, Any]:
    if 'error' in data:
        raise ValueError(f"api error: {data.get('message')}")
    return data.get('result', {})