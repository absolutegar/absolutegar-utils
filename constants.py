from typing import Final, Dict

CACHE_TTL_SECONDS: Final[int] = 3600
MAX_RETRIES: Final[int] = 3
PRECISION_LIMIT: Final[int] = 18

CRYPTO_PAIRS: Final[Dict[str, str]] = {
    'BTC': 'bitcoin',
    'ETH': 'ethereum',
    'SOL': 'solana',
    'DOT': 'polkadot',
    'ADA': 'cardano'
}

RPC_TIMEOUT: Final[float] = 5.0
BATCH_SIZE: Final[int] = 100

def get_precision_multiplier(decimals: int = PRECISION_LIMIT) -> int:
    return 10**decimals

SUPPORTED_NETWORKS: Final[tuple] = ('mainnet', 'testnet', 'devnet')
DEFAULT_HEADERS: Final[Dict[str, str]] = {
    'Content-Type': 'application/json',
    'User-Agent': 'absolutegar-utils/1.0.0'
}