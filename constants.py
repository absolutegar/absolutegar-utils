from typing import Final

# Network constants
MAINNET_CHAIN_ID: Final[int] = 1
TESTNET_CHAIN_ID: Final[int] = 11155111

# Transaction defaults
GAS_LIMIT_DEFAULT: Final[int] = 21000
MAX_RETRIES: Final[int] = 3
TIMEOUT_SECONDS: Final[int] = 30

# Crypto asset identifiers
BTC_SYMBOL: Final[str] = "BTC"
ETH_SYMBOL: Final[str] = "ETH"

# Precision settings
WEI_PER_ETHER: Final[int] = 10**18
SATOSHI_PER_BTC: Final[int] = 10**8

# Error messages
ERR_CONNECTION_FAILED: Final[str] = "failed to connect to node"
ERR_INVALID_ADDRESS: Final[str] = "invalid wallet address format"
ERR_INSUFFICIENT_FUNDS: Final[str] = "insufficient balance for transaction"

# Configuration paths
DEFAULT_CONFIG_PATH: Final[str] = "./config/settings.json"
LOG_DIR: Final[str] = "./logs"