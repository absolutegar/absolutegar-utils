import hashlib
import hmac
from decimal import Decimal
from typing import Any

def generate_signature(api_secret: str, message: str) -> str:
    return hmac.new(
        api_secret.encode('utf-8'),
        message.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def format_crypto_amount(amount: Any, precision: int = 8) -> Decimal:
    return Decimal(str(amount)).quantize(Decimal(f'1.{"0" * precision}'))

def validate_ticker(ticker: str) -> bool:
    return bool(ticker and ticker.isalnum() and len(ticker) <= 10)

def calculate_profit_margin(buy_price: float, sell_price: float) -> float:
    if buy_price <= 0:
        return 0.0
    return ((sell_price - buy_price) / buy_price) * 100

def parse_order_id(raw_id: Any) -> str:
    return str(raw_id).strip().upper()