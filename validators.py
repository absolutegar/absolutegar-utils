import re
from typing import Union


def validate_address(address: str) -> bool:
    """Validate cryptocurrency wallet address format."""
    pattern = re.compile(r"^0x[a-fA-F0-9]{40}$")
    return bool(pattern.match(address))


def validate_amount(amount: Union[int, float]) -> bool:
    """Validate non-negative transaction amount."""
    return isinstance(amount, (int, float)) and amount >= 0


def validate_gas_limit(gas: int) -> bool:
    """Validate integer gas limit bounds."""
    return isinstance(gas, int) and 21000 <= gas <= 10000000


def validate_hex(data: str) -> bool:
    """Validate raw hex string encoding."""
    pattern = re.compile(r"^[a-fA-F0-9]+$")
    return bool(pattern.match(data))