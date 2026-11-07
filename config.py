import os
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Optional

DEFAULT_CONFIG: Dict[str, Any] = {
    "network": "mainnet",
    "rpc_url": "https://cloudflare-eth.com",
    "timeout": 30,
    "max_retries": 3,
    "gas_multiplier": 1.1,
    "enable_cache": True,
}


@dataclass
class Config:
    network: str = "mainnet"
    rpc_url: str = "https://cloudflare-eth.com"
    timeout: int = 30
    max_retries: int = 3
    gas_multiplier: float = 1.1
    enable_cache: bool = True

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Config":
        valid_keys = {f.name for f in cls.__dataclass_fields__.values()}
        filtered = {k: v for k, v in data.items() if k in valid_keys}
        return cls(**filtered)


class ConfigLoader:
    def __init__(self, config_path: Optional[str] = None):
        self.config_path = Path(config_path) if config_path else None

    def load(self) -> Config:
        merged = DEFAULT_CONFIG.copy()

        if self.config_path and self.config_path.is_file():
            with open(self.config_path, "r", encoding="utf-8") as f:
                file_data = json.load(f)
                merged.update(file_data)

        env_mappings = {
            "CRYPTO_NETWORK": ("network", str),
            "CRYPTO_RPC_URL": ("rpc_url", str),
            "CRYPTO_TIMEOUT": ("timeout", int),
            "CRYPTO_MAX_RETRIES": ("max_retries", int),
            "CRYPTO_GAS_MULTIPLIER": ("gas_multiplier", float),
        }

        for env_var, (key, cast_type) in env_mappings.items():
            val = os.getenv(env_var)
            if val is not None:
                merged[key] = cast_type(val)

        return Config.from_dict(merged)
