from decimal import Decimal, ROUND_HALF_UP
from typing import Union

SATOSHI_PER_BTC = 100_000_000


def satoshi_to_btc(satoshis: int) -> Decimal:
    """Convert an amount in satoshis to Bitcoin (BTC)."""
    if satoshis < 0:
        raise ValueError("Satoshis cannot be negative")
    return (Decimal(satoshis) / Decimal(SATOSHI_PER_BTC)).quantize(
        Decimal("0.00000001")
    )


def btc_to_satoshi(btc: Union[int, float, str, Decimal]) -> int:
    """Convert an amount in Bitcoin (BTC) to satoshis."""
    amount = Decimal(str(btc))
    if amount < 0:
        raise ValueError("BTC amount cannot be negative")
    return int((amount * Decimal(SATOSHI_PER_BTC)).to_integral_value(rounding=ROUND_HALF_UP))


def calculate_tx_fee(vbytes: int, sat_per_vbyte: float) -> int:
    """Calculate transaction fee in satoshis based on size and rate."""
    if vbytes <= 0 or sat_per_vbyte < 0:
        raise ValueError("Invalid transaction dimensions or fee rate")
    return int(Decimal(str(vbytes)) * Decimal(str(sat_per_vbyte)))


def truncate_hash(hash_str: str, leading: int = 6, trailing: int = 4) -> str:
    """Truncate a cryptographic hash or address for display purposes."""
    if len(hash_str) <= leading + trailing:
        return hash_str
    return f"{hash_str[:leading]}...{hash_str[-trailing:]}"
