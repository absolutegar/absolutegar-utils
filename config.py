import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, default_path: str = "config.json"):
        self.path = default_path
        self.defaults = {
            "rpc_url": "https://mainnet.infura.io/v3/",
            "timeout": 30,
            "retry_attempts": 3
        }

    def load(self) -> Dict[str, Any]:
        if not os.path.exists(self.path):
            return self.defaults
        try:
            with open(self.path, "r") as f:
                data = json.load(f)
            return {**self.defaults, **data}
        except (json.JSONDecodeError, IOError):
            return self.defaults

def get_config(path: str = "config.json") -> Dict[str, Any]:
    loader = ConfigLoader(path)
    return loader.load()