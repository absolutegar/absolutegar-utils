import time
import functools
from typing import Callable, Any

def retry(retries: int = 3, delay: float = 1.0, exceptions: tuple = (Exception,)): 
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    time.sleep(delay * (2 ** attempt))
            raise last_exception
        return wrapper
    return decorator

def network_request(url: str, session: Any) -> dict:
    @retry(retries=3, delay=0.5)
    def fetch():
        response = session.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    return fetch()