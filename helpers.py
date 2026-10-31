from typing import List, Dict, Union
from decimal import Decimal, ROUND_HALF_UP

def normalize_amount(amount: Union[str, float, int], precision: int = 8) -> Decimal:
    return Decimal(str(amount)).quantize(Decimal(10) ** -precision, rounding=ROUND_HALF_UP)

def format_orderbook(data: List[Dict[str, Union[str, float]]], side: str) -> List[Dict[str, Decimal]]:
    return [
        {
            'price': normalize_amount(entry['p']),
            'size': normalize_amount(entry['s'])
        }
        for entry in data
        if entry.get('side') == side
    ]

def calculate_position_value(size: Decimal, price: Decimal) -> Decimal:
    return (size * price).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

def validate_ticker(symbol: str) -> bool:
    return bool(symbol and isinstance(symbol, str) and '/' in symbol)