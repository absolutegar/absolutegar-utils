import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "RPC_URL": "https://mainnet.infura.io/v3/",
    "TIMEOUT": 30,
    "MAX_RETRIES": 3,
    "DEBUG": False
}

class ConfigLoader:
    def __init__(self, env_prefix: str = "AG_"):
        self.env_prefix = env_prefix
        self.settings = DEFAULT_CONFIG.copy()
        self._load_from_env()

    def _load_from_env(self) -> None:
        for key in DEFAULT_CONFIG:
            env_key = f"{self.env_prefix}{key}"
            value = os.getenv(env_key)
            if value is not None:
                self.settings[key] = self._cast_type(key, value)

    def _cast_type(self, key: str, value: str) -> Any:
        default_val = DEFAULT_CONFIG[key]
        if isinstance(default_val, bool):
            return value.lower() in ("true", "1", "yes")
        if isinstance(default_val, int):
            return int(value)
        return value

    def get(self, key: str, default: Any = None) -> Any:
        return self.settings.get(key, default)

config = ConfigLoader()