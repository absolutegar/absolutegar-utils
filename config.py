import os
import json
from typing import Any, Dict, Optional

DEFAULT_CONFIG: Dict[str, Any] = {
    "network": "mainnet",
    "rpc_url": "https://eth-mainnet.g.alchemy.com/v2/demo",
    "request_timeout": 30,
    "max_retries": 3,
    "gas_limit_multiplier": 1.1,
    "enable_cache": True,
}


class ConfigLoader:
    def __init__(self, config_path: Optional[str] = None):
        self.config_path = config_path
        self._config = DEFAULT_CONFIG.copy()
        self._load()

    def _load(self) -> None:
        if self.config_path and os.path.exists(self.config_path):
            with open(self.config_path, "r", encoding="utf-8") as f:
                file_config = json.load(f)
                self._config.update(file_config)
        self._apply_env_overrides()

    def _apply_env_overrides(self) -> None:
        env_mapping = {
            "CRYPTO_NETWORK": ("network", str),
            "CRYPTO_RPC_URL": ("rpc_url", str),
            "CRYPTO_TIMEOUT": ("request_timeout", int),
            "CRYPTO_MAX_RETRIES": ("max_retries", int),
        }
        for env_var, (config_key, cast_type) in env_mapping.items():
            val = os.getenv(env_var)
            if val is not None:
                try:
                    self._config[config_key] = cast_type(val)
                except ValueError:
                    pass

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)

    def as_dict(self) -> Dict[str, Any]:
        return self._config.copy()
