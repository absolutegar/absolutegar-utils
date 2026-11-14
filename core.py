import asyncio
import functools
import logging
import random
from typing import Any, Callable, Tuple, Type, Union

logger = logging.getLogger("absolutegar.core")


class NetworkError(Exception):
    """Raised when network operation fails after retries."""


def retry_network_op(
    retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    jitter: bool = True,
    exceptions: Union[Type[Exception], Tuple[Type[Exception], ...]] = (Exception,),
) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            for attempt in range(1, retries + 1):
                try:
                    return await func(*args, **kwargs)
                except exceptions as err:
                    if attempt == retries:
                        logger.error(f"{func.__name__} failed on final attempt {attempt}/{retries}: {err}")
                        raise NetworkError(f"{func.__name__} failed after {retries} attempts") from err
                    sleep_time = current_delay + (random.uniform(0, current_delay) if jitter else 0)
                    logger.warning(f"{func.__name__} attempt {attempt} failed: {err}. Retrying in {sleep_time:.2f}s")
                    await asyncio.sleep(sleep_time)
                    current_delay *= backoff
        return wrapper
    return decorator
