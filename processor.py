import hashlib
import hmac
from decimal import Decimal
from typing import Any, Dict

def normalize_amount(amount: str | float) -> Decimal:
    return Decimal(str(amount)).quantize(Decimal('1.00000000'))

def generate_signature(api_secret: str, payload: str) -> str:
    return hmac.new(
        api_secret.encode('utf-8'),
        payload.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def parse_crypto_pair(pair: str) -> tuple[str, str]:
    parts = pair.upper().split('_')
    if len(parts) != 2:
        raise ValueError('Invalid pair format')
    return parts[0], parts[1]

def clean_order_data(data: Dict[str, Any]) -> Dict[str, Any]:
    return {
        'symbol': data['symbol'].upper(),
        'side': data['side'].lower(),
        'quantity': str(normalize_amount(data['quantity'])),
        'price': str(normalize_amount(data['price']))
    }