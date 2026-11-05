import os
from typing import Final
from dotenv import load_dotenv

load_dotenv()

RPC_URL: Final[str] = os.getenv("RPC_URL", "https://eth.llamarpc.com")
CHAIN_ID: Final[int] = int(os.getenv("CHAIN_ID", "1"))
GAS_MULTIPLIER: Final[float] = float(os.getenv("GAS_MULTIPLIER", "1.2"))

REQUIRED_ENV_VARS: Final[list[str]] = ["PRIVATE_KEY", "RPC_URL"]

def validate_config() -> None:
    missing = [var for var in REQUIRED_ENV_VARS if not os.getenv(var)]
    if missing:
        raise EnvironmentError(f"Missing required env vars: {', '.join(missing)}")

class ChainConfig:
    def __init__(self, rpc: str, chain_id: int):
        self.rpc = rpc
        self.chain_id = chain_id

def get_chain_config() -> ChainConfig:
    validate_config()
    return ChainConfig(RPC_URL, CHAIN_ID)