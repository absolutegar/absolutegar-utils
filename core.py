from decimal import Decimal, ROUND_HALF_UP
from typing import Union, Dict

def normalize_amount(amount: Union[str, float, Decimal], precision: int = 8) -> Decimal:
    """Format crypto values to standard decimal precision."""
    val = Decimal(str(amount))
    return val.quantize(Decimal(f'1.{"0" * precision}'), rounding=ROUND_HALF_UP)

def calculate_fee(amount: Decimal, rate: Decimal) -> Decimal:
    """Compute transaction fee from decimal amounts."""
    return (amount * rate).quantize(Decimal('0.00000001'), rounding=ROUND_HALF_UP)

def format_orderbook(data: Dict) -> Dict:
    """Standardize exchange orderbook keys to floats."""
    return {
        'bids': [[float(p), float(a)] for p, a in data.get('bids', [])],
        'asks': [[float(p), float(a)] for p, a in data.get('asks', [])]
    }

class CryptoConverter:
    @staticmethod
    def to_base_unit(amount: Decimal, decimals: int) -> int:
        return int(amount * (10 ** decimals))

    @staticmethod
    def from_base_unit(amount: int, decimals: int) -> Decimal:
        return Decimal(amount) / (10 ** decimals)