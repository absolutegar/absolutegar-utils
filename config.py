import os
from typing import Dict, Any, Optional

class Config:
    """Centralized configuration management for crypto utilities."""

    def __init__(self, env: str = "production") -> None:
        self.env: str = env
        self.settings: Dict[str, Any] = {
            "rpc_url": os.getenv("RPC_URL", "https://mainnet.infura.io/v3/"),
            "timeout": int(os.getenv("REQUEST_TIMEOUT", "30")),
            "retry_limit": int(os.getenv("RETRY_LIMIT", "3")),
            "debug": os.getenv("DEBUG", "false").lower() == "true"
        }

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """Retrieve a specific configuration value."""
        return self.settings.get(key, default)

    def update(self, key: str, value: Any) -> None:
        """Update an existing configuration setting."""
        self.settings[key] = value

def load_config() -> Config:
    """Factory function for creating a Config instance."""
    return Config(env=os.getenv("APP_ENV", "production"))