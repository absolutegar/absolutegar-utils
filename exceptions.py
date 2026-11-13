import time
import functools
from typing import Callable, Any, Type, Tuple

class NetworkRetryError(Exception):
    """Exception raised for network operation retries."""

def retry(exceptions: Tuple[Type[Exception], ...] = (Exception,), 
          retries: int = 3, 
          delay: float = 1.0) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for i in range(retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    time.sleep(delay * (2 ** i))
            raise NetworkRetryError(f"Max retries {retries} reached") from last_exception
        return wrapper
    return decorator