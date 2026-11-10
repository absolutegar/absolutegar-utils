from decimal import Decimal
from typing import Dict, Final, Tuple

CHAIN_ID_ETHEREUM: Final[int] = 1
CHAIN_ID_OPTIMISM: Final[int] = 10
CHAIN_ID_BSC: Final[int] = 56
CHAIN_ID_POLYGON: Final[int] = 137
CHAIN_ID_ARBITRUM: Final[int] = 42161

TOKEN_DECIMALS: Final[Dict[str, int]] = {
    "BTC": 8,
    "ETH": 18,
    "USDT": 6,
    "USDC": 6,
    "DAI": 18,
    "WBTC": 8,
    "SOL": 9,
}

WEI_PER_ETH: Final[Decimal] = Decimal("1000000000000000000")
SATOSHI_PER_BTC: Final[Decimal] = Decimal("100000000")
GWEI_PER_ETH: Final[Decimal] = Decimal("1000000000")

DEFAULT_RPC_URLS: Final[Dict[int, str]] = {
    CHAIN_ID_ETHEREUM: "https://ethereum.publicnode.com",
    CHAIN_ID_OPTIMISM: "https://mainnet.optimism.io",
    CHAIN_ID_BSC: "https://bsc-dataseed.binance.org",
    CHAIN_ID_POLYGON: "https://polygon-rpc.com",
    CHAIN_ID_ARBITRUM: "https://arb1.arbitrum.io/rpc",
}

STABLECOIN_SYMBOLS: Final[Tuple[str, ...]] = ("USDT", "USDC", "DAI", "BUSD", "FRAX")
