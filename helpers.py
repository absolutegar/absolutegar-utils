from decimal import Decimal, ROUND_DOWN
import re

SATO_FACTOR = Decimal("100000000")
WEI_FACTOR = Decimal("1000000000000000000")


def satoshi_to_btc(sats: int) -> Decimal:
    return Decimal(sats) / SATO_FACTOR


def btc_to_satoshi(btc: Decimal | float | str) -> int:
    return int((Decimal(str(btc)) * SATO_FACTOR).quantize(Decimal("1"), rounding=ROUND_DOWN))


def wei_to_eth(wei: int) -> Decimal:
    return Decimal(wei) / WEI_FACTOR


def eth_to_wei(eth: Decimal | float | str) -> int:
    return int((Decimal(str(eth)) * WEI_FACTOR).quantize(Decimal("1"), rounding=ROUND_DOWN))


def truncate_address(address: str, prefix_len: int = 6, suffix_len: int = 4) -> str:
    if not address or len(address) <= prefix_len + suffix_len:
        return address
    return f"{address[:prefix_len]}...{address[-suffix_len:]}"


def calculate_slippage(price: Decimal | float, percentage: float, is_buy: bool = True) -> Decimal:
    p = Decimal(str(price))
    adj = Decimal(str(percentage / 100))
    factor = (Decimal("1") + adj) if is_buy else (Decimal("1") - adj)
    return p * factor


def is_valid_hex_tx(tx_hash: str) -> bool:
    clean = tx_hash.removeprefix("0x")
    return len(clean) == 64 and bool(re.match(r"^[0-9a-fA-F]+$", clean))
