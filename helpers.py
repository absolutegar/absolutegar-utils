from decimal import Decimal, ROUND_DOWN
from typing import Union

UNITS = {
    "wei": 1,
    "gwei": 10**9,
    "ether": 10**18,
}


def to_wei(amount: Union[int, float, str], unit: str = "ether") -> int:
    unit_lower = unit.lower()
    if unit_lower not in UNITS:
        raise ValueError(f"Unknown unit: {unit}")
    dec_amount = Decimal(str(amount))
    return int(dec_amount * UNITS[unit_lower])


def from_wei(amount: int, unit: str = "ether") -> Decimal:
    unit_lower = unit.lower()
    if unit_lower not in UNITS:
        raise ValueError(f"Unknown unit: {unit}")
    return Decimal(amount) / Decimal(UNITS[unit_lower])


def calculate_slippage(expected_price: float, actual_price: float) -> float:
    if expected_price <= 0:
        raise ValueError("Expected price must be positive")
    return ((actual_price - expected_price) / expected_price) * 100.0


def normalize_symbol(symbol: str) -> str:
    return symbol.upper().replace("-", "").replace("_", "").replace("/", "")


def truncate_precision(val: Union[float, str, Decimal], decimals: int) -> Decimal:
    fmt = "0." + "0" * decimals if decimals > 0 else "0"
    return Decimal(str(val)).quantize(Decimal(fmt), rounding=ROUND_DOWN)
