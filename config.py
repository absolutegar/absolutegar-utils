import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, defaults: Dict[str, Any] = None):
        self.defaults = defaults or {}
        self._config: Dict[str, Any] = {}

    def load(self, path: str) -> None:
        if not os.path.exists(path):
            self._config = self.defaults.copy()
            return

        with open(path, 'r') as f:
            data = json.load(f)
            self._config = {**self.defaults, **data}

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)

    @property
    def all(self) -> Dict[str, Any]:
        return self._config.copy()