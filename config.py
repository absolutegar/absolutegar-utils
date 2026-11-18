import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, default_path: str = "config.json"):
        self.path = default_path
        self.defaults = {
            "rpc_url": "https://mainnet.infura.io/v3/",
            "timeout": 30,
            "max_retries": 3,
            "debug": False
        }

    def load(self) -> Dict[str, Any]:
        config = self.defaults.copy()
        if os.path.exists(self.path):
            try:
                with open(self.path, "r") as f:
                    user_config = json.load(f)
                    config.update(user_config)
            except (json.JSONDecodeError, IOError):
                pass
        return config

def get_config() -> Dict[str, Any]:
    loader = ConfigLoader()
    return loader.load()