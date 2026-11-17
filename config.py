import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "rpc_url": "https://mainnet.infura.io/v3/",
    "timeout": 30,
    "retry_limit": 3,
    "fee_buffer": 0.001
}

class ConfigLoader:
    def __init__(self, path: str = "config.json"):
        self.path = path
        self.data = self._load()

    def _load(self) -> Dict[str, Any]:
        if not os.path.exists(self.path):
            return DEFAULT_CONFIG
        with open(self.path, "r") as f:
            try:
                user_config = json.load(f)
                return {**DEFAULT_CONFIG, **user_config}
            except json.JSONDecodeError:
                return DEFAULT_CONFIG

    def get(self, key: str, default: Any = None) -> Any:
        return self.data.get(key, default)

    @property
    def all(self) -> Dict[str, Any]:
        return self.data.copy()