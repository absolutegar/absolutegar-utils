from typing import Final

# Network identifiers
MAINNET_ID: Final[str] = 'mainnet'
TESTNET_ID: Final[str] = 'testnet'

# Precision settings
SATOSHI_UNIT: Final[int] = 100_000_000
WEI_UNIT: Final[int] = 10**18

# Timeouts and intervals
DEFAULT_TIMEOUT: Final[float] = 30.0
RETRY_DELAY: Final[float] = 2.0
MAX_RETRIES: Final[int] = 3

# Regex patterns
ADDRESS_PATTERN_BTC: Final[str] = r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$'
ADDRESS_PATTERN_ETH: Final[str] = r'^0x[a-fA-F0-9]{40}$'

# Default headers
USER_AGENT: Final[str] = 'absolutegar-utils/1.0.0'
HEADERS: Final[dict[str, str]] = {
    'User-Agent': USER_AGENT,
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}