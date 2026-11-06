import hashlib
import hmac
import base64
from typing import Dict, Any

def generate_signature(api_secret: str, message: str) -> str:
    return hmac.new(
        api_secret.encode('utf-8'),
        message.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def format_order_payload(symbol: str, side: str, amount: float, price: float) -> Dict[str, Any]:
    return {
        "symbol": symbol.upper(),
        "side": side.lower(),
        "quantity": str(amount),
        "price": str(price),
        "timestamp": None
    }

def encode_auth_header(api_key: str, secret: str) -> str:
    credentials = f"{api_key}:{secret}"
    return base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

def validate_price_precision(price: float, tick_size: float) -> bool:
    return (price / tick_size).is_integer()

def calculate_position_size(balance: float, risk_percentage: float, stop_loss_pct: float) -> float:
    risk_amount = balance * (risk_percentage / 100)
    return risk_amount / (stop_loss_pct / 100)