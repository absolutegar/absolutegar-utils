from decimal import Decimal, InvalidOperation
from typing import Union


class CryptoValueError(ValueError):
    pass


def parse_satoshi(val: Union[int, float, str, Decimal]) -> int:
    if val is None:
        raise CryptoValueError("Value cannot be None")
    try:
        if isinstance(val, float):
            val = str(val)
        d_val = Decimal(str(val))
    except (InvalidOperation, TypeError) as e:
        raise CryptoValueError(f"Invalid numeric input: {val}") from e

    if d_val < 0:
        raise CryptoValueError(f"Amount cannot be negative: {val}")

    satoshis = d_val * Decimal("100000000")
    if satoshis != satoshis.quantize(Decimal("1")):
        raise CryptoValueError(f"Sub-satoshi precision not allowed: {val}")

    return int(satoshis)


def safe_hex_to_bytes(hex_str: str) -> bytes:
    if not isinstance(hex_str, str):
        raise TypeError("Input must be a string")
    clean_hex = hex_str.lower()
    if clean_hex.startswith("0x"):
        clean_hex = clean_hex[2:]
    if len(clean_hex) % 2 != 0:
        clean_hex = "0" + clean_hex
    try:
        return bytes.fromhex(clean_hex)
    except ValueError as e:
        raise CryptoValueError(f"Invalid hex string: {hex_str}") from e


def format_crypto_amount(amount: Union[int, Decimal], decimals: int = 8) -> str:
    if not isinstance(decimals, int) or not (0 <= decimals <= 18):
        raise ValueError("Decimals must be an integer between 0 and 18")
    try:
        d_amount = Decimal(str(amount))
    except (InvalidOperation, TypeError) as e:
        raise CryptoValueError(f"Invalid amount to format: {amount}") from e

    factor = Decimal(10) ** decimals
    scaled = d_amount / factor
    return f"{scaled:.{decimals}f}"
