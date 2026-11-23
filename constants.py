from typing import Final, Dict, List

# Network identifiers
MAINNET: Final[str] = "mainnet"
TESTNET: Final[str] = "testnet"

# Supported precision configurations
DEFAULT_PRECISION: Final[int] = 8
MAX_DECIMAL_PLACES: Final[int] = 18

# Asset classification mappings
ASSET_TYPES: Final[Dict[str, str]] = {
    "BTC": "native",
    "ETH": "native",
    "ERC20": "token",
    "BEP20": "token"
}

# Standardized API response status codes
STATUS_SUCCESS: Final[int] = 200
STATUS_BAD_REQUEST: Final[int] = 400
STATUS_UNAUTHORIZED: Final[int] = 401
STATUS_RATE_LIMIT: Final[int] = 429

# Gas estimation parameters
MIN_GAS_LIMIT: Final[int] = 21000
DEFAULT_GAS_MULTIPLIER: Final[float] = 1.2

# Supported network list
SUPPORTED_NETWORKS: Final[List[str]] = [MAINNET, TESTNET]

# Validation constraints
MIN_ADDRESS_LENGTH: Final[int] = 26
MAX_ADDRESS_LENGTH: Final[int] = 66