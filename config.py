import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "rpc_url": "https://api.mainnet-beta.solana.com",
    "timeout": 30,
    "retry_attempts": 3
}

class ConfigLoader:
    def __init__(self, path: str = "config.json"):
        self.path = path
        self.config = self._load()

    def _load(self) -> Dict[str, Any]:
        if not os.path.exists(self.path):
            return DEFAULT_CONFIG
        
        try:
            with open(self.path, "r") as f:
                user_config = json.load(f)
                return {**DEFAULT_CONFIG, **user_config}
        except (json.JSONDecodeError, IOError):
            return DEFAULT_CONFIG

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)

    def __getitem__(self, key: str) -> Any:
        return self.config[key]