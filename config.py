import os
import json
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, defaults: Dict[str, Any] = None):
        self.defaults = defaults or {}

    def load(self, file_path: str) -> Dict[str, Any]:
        config = self.defaults.copy()
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                try:
                    file_data = json.load(f)
                    config.update(file_data)
                except json.JSONDecodeError:
                    pass
        return config

def get_env_config(key: str, default: Any = None) -> Any:
    return os.getenv(key, default)

def load_app_config(path: str = 'config.json') -> Dict[str, Any]:
    defaults = {
        'rpc_url': 'https://mainnet.infura.io/v3/default',
        'timeout': 30,
        'retries': 3
    }
    loader = ConfigLoader(defaults)
    return loader.load(path)