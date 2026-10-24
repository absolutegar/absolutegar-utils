from typing import Tuple


def satoshi_to_btc(satoshis: int) -> float:
    if satoshis < 0:
        raise ValueError("Satoshis cannot be negative")
    return satoshis / 100_000_000


def btc_to_satoshi(btc: float) -> int:
    if btc < 0:
        raise ValueError("BTC amount cannot be negative")
    return int(round(btc * 100_000_000))


def calculate_pnl(
    entry_price: float, exit_price: float, amount: float, is_long: bool = True
) -> Tuple[float, float]:
    if entry_price <= 0 or exit_price < 0 or amount <= 0:
        raise ValueError("Prices and amount must be positive numbers")

    direction = 1 if is_long else -1
    pnl = (exit_price - entry_price) * amount * direction
    roi = ((exit_price - entry_price) / entry_price) * 100 * direction
    return round(pnl, 8), round(roi, 2)


def truncate_address(address: str, leading: int = 6, trailing: int = 4) -> str:
    if not address or len(address) <= (leading + trailing):
        return address
    return f"{address[:leading]}...{address[-trailing:]}"


def normalize_symbol(symbol: str) -> str:
    cleaned = symbol.strip().upper().replace("/", "").replace("-", "")
    if not cleaned:
        raise ValueError("Invalid trading symbol")
    return cleaned
