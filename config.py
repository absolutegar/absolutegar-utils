import os
import json
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, defaults: Dict[str, Any], env_prefix: str = "AGAR_"):
        self.config = defaults.copy()
        self.env_prefix = env_prefix

    def load_from_file(self, path: str) -> None:
        if os.path.exists(path):
            with open(path, "r") as f:
                self.config.update(json.load(f))

    def load_from_env(self) -> None:
        for key in self.config.keys():
            env_key = f"{self.env_prefix}{key.upper()}"
            value = os.getenv(env_key)
            if value is not None:
                self.config[key] = self._parse_value(value)

    def _parse_value(self, value: str) -> Any:
        try:
            return json.loads(value)
        except (json.JSONDecodeError, TypeError):
            return value

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)

def get_config(defaults: Dict[str, Any], path: str = "config.json") -> ConfigLoader:
    loader = ConfigLoader(defaults)
    loader.load_from_file(path)
    loader.load_from_env()
    return loader