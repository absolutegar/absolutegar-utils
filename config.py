import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, defaults: Dict[str, Any], config_path: str = "config.json"):
        self.defaults = defaults
        self.config_path = config_path
        self.config = self._load()

    def _load(self) -> Dict[str, Any]:
        if not os.path.exists(self.config_path):
            return self.defaults
        try:
            with open(self.config_path, "r") as f:
                user_config = json.load(f)
            return {**self.defaults, **user_config}
        except (json.JSONDecodeError, IOError):
            return self.defaults

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)

    def __getitem__(self, key: str) -> Any:
        return self.config[key]