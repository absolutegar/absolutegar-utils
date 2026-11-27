import decimal
from typing import Dict, Any, Optional

def normalize_crypto_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """Standardizes financial precision for crypto payloads."""
    context = decimal.Context(prec=28, rounding=decimal.ROUND_HALF_UP)
    normalized = {}
    
    for key, value in data.items():
        if isinstance(value, (int, float, str)) and key in ('price', 'amount', 'fee'):
            try:
                normalized[key] = context.create_decimal(str(value))
            except (decimal.InvalidOperation, ValueError):
                normalized[key] = None
        else:
            normalized[key] = value
    return normalized

def validate_order_payload(data: Dict[str, Any]) -> bool:
    required_keys = {'symbol', 'price', 'amount'}
    return required_keys.issubset(data.keys()) and all(data.values())

def format_ticker(symbol: str) -> str:
    return symbol.upper().replace('/', '_')
