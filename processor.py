import hashlib
import hmac
from decimal import Decimal
from typing import Any, Dict

def calculate_signature(secret: str, message: str) -> str:
    return hmac.new(secret.encode(), message.encode(), hashlib.sha256).hexdigest()

def normalize_amount(amount: Any) -> Decimal:
    try:
        return Decimal(str(amount)).normalize()
    except Exception:
        return Decimal('0')

def validate_payload(data: Dict[str, Any], required_keys: list[str]) -> bool:
    return all(key in data for key in required_keys)

def format_price(price: Decimal, precision: int = 8) -> str:
    return format(price, f'.{precision}f')

def aggregate_balances(balances: list[Dict[str, Any]]) -> Dict[str, Decimal]:
    summary: Dict[str, Decimal] = {}
    for entry in balances:
        asset = entry.get('asset', 'unknown')
        amount = normalize_amount(entry.get('amount', 0))
        summary[asset] = summary.get(asset, Decimal(0)) + amount
    return summary