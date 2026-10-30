from typing import Final, Dict, List

# Network identifiers for crypto transactions
MAINNET_CHAIN_ID: Final[int] = 1
TESTNET_CHAIN_ID: Final[int] = 11155111

# API request rate limits
MAX_RETRIES: Final[int] = 3
REQUEST_TIMEOUT_SECONDS: Final[float] = 30.0

# Supported crypto protocols
SUPPORTED_PROTOCOLS: Final[List[str]] = ['erc20', 'bep20', 'solana']

# Default gas multiplier
GAS_BUFFER_PERCENTAGE: Final[float] = 1.2

# Mapping of protocol to fee decimal precision
FEE_PRECISION_MAP: Final[Dict[str, int]] = {
    'erc20': 18,
    'bep20': 18,
    'solana': 9
}

def get_chain_name(chain_id: int) -> str:
    """Return human readable chain name from ID."""
    mapping: Dict[int, str] = {
        MAINNET_CHAIN_ID: "mainnet",
        TESTNET_CHAIN_ID: "sepolia"
    }
    return mapping.get(chain_id, "unknown")
