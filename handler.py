import time
import functools
from typing import Callable, Any, Type, Tuple

def retry(exceptions: Tuple[Type[Exception], ...], tries: int = 3, delay: float = 1.0) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempt = 0
            while attempt < tries:
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    attempt += 1
                    if attempt >= tries:
                        raise
                    time.sleep(delay)
            return None
        return wrapper
    return decorator

class NetworkHandler:
    @staticmethod
    @retry(exceptions=(ConnectionError, TimeoutError), tries=3, delay=2.0)
    def fetch_data(url: str) -> dict:
        import requests
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()