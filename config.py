import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "RPC_URL": "https://mainnet.infura.io/v3/",
    "TIMEOUT": 30,
    "MAX_RETRIES": 3,
    "DEBUG": False
}

class ConfigLoader:
    def __init__(self, env_prefix: str = "AGAR"):
        self.prefix = env_prefix

    def get(self, key: str) -> Any:
        env_key = f"{self.prefix}_{key}"
        return os.getenv(env_key, DEFAULT_CONFIG.get(key))

    def load_all(self) -> Dict[str, Any]:
        return {key: self.get(key) for key in DEFAULT_CONFIG}

config = ConfigLoader()