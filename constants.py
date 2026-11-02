from typing import Final
from enum import IntEnum

CACHE_TTL: Final[int] = 3600
MAX_RETRIES: Final[int] = 3
PRECISION: Final[int] = 18

class ChainID(IntEnum):
    ETHEREUM = 1
    OPTIMISM = 10
    ARBITRUM = 42161

HTTP_TIMEOUT: Final[float] = 10.0
CHUNK_SIZE: Final[int] = 1024

SUPPORTED_ASSETS: Final[tuple[str, ...]] = (
    'ETH',
    'USDC',
    'USDT',
    'WBTC',
    'DAI'
)

GAS_BUFFER_MULTIPLIER: Final[float] = 1.2
NONCE_CACHE_KEY: Final[str] = 'addr_nonce_map'
