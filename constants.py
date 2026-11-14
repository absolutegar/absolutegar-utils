from typing import Final

# Network identifiers
MAINNET_ID: Final[str] = "0x1"
TESTNET_ID: Final[str] = "0xaa36a7"

# Transaction defaults
DEFAULT_GAS_LIMIT: Final[int] = 21000
MAX_RETRIES: Final[int] = 3
TIMEOUT_SECONDS: Final[int] = 30

# API endpoints
INFURA_BASE_URL: Final[str] = "https://mainnet.infura.io/v3/"
ALCHEMY_BASE_URL: Final[str] = "https://eth-mainnet.g.alchemy.com/v2/"

# Crypto currency constants
WEI_PER_ETHER: Final[int] = 10**18
GWEI_PER_ETHER: Final[int] = 10**9

# Error messages
ERR_CONNECTION_FAILED: Final[str] = "network connection failed"
ERR_INVALID_ADDRESS: Final[str] = "provided address format is invalid"
ERR_INSUFFICIENT_FUNDS: Final[str] = "account balance too low for operation"

# Supported protocols
PROTOCOLS: Final[list[str]] = ["erc20", "erc721", "erc1155"]