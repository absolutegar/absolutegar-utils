import os
from typing import Any, Dict, Optional

DEFAULT_CONFIG: Dict[str, Any] = {
    "RPC_URL": "https://mainnet.infura.io/v3/",
    "TIMEOUT": 30,
    "MAX_RETRIES": 3,
    "DEBUG": False
}

class ConfigLoader:
    def __init__(self, overrides: Optional[Dict[str, Any]] = None):
        self._config = DEFAULT_CONFIG.copy()
        if overrides:
            self._config.update(overrides)
        self._load_from_env()

    def _load_from_env(self) -> None:
        for key in self._config:
            env_val = os.getenv(f"ABSOLUTEGAR_{key}")
            if env_val:
                self._config[key] = self._cast_value(key, env_val)

    def _cast_value(self, key: str, value: str) -> Any:
        default = self._config[key]
        if isinstance(default, bool):
            return value.lower() in ("true", "1", "yes")
        if isinstance(default, int):
            return int(value)
        return value

    def get(self, key: str) -> Any:
        return self._config.get(key)

def get_config() -> ConfigLoader:
    return ConfigLoader()