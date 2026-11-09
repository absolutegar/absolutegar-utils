from typing import Dict, List, Any, Optional
from decimal import Decimal, InvalidOperation

def normalize_crypto_amount(amount: Any) -> Decimal:
    try:
        return Decimal(str(amount)).quantize(Decimal('1.00000000'))
    except (InvalidOperation, ValueError):
        return Decimal('0.00000000')

def validate_ticker_format(ticker: str) -> bool:
    if not isinstance(ticker, str) or len(ticker) < 2 or len(ticker) > 10:
        return False
    return ticker.isalnum()

def format_order_payload(symbol: str, side: str, amount: Decimal, price: Decimal) -> Dict[str, Any]:
    return {
        'symbol': symbol.upper(),
        'side': side.lower(),
        'quantity': str(amount),
        'price': str(price),
        'type': 'LIMIT'
    }

def aggregate_balances(data: List[Dict[str, Any]]) -> Dict[str, Decimal]:
    balances: Dict[str, Decimal] = {}
    for entry in data:
        asset = entry.get('asset')
        if asset:
            amount = normalize_crypto_amount(entry.get('free', 0))
            balances[asset] = balances.get(asset, Decimal('0')) + amount
    return balances