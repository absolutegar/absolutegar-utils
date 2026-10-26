import asyncio
import functools
import logging
import random
from typing import Any, Callable, Tuple, Type

logger = logging.getLogger(__name__)


def retry_async(
    retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: Tuple[Type[Exception], ...] = (Exception,),
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
                        logger.error(
                            f"Operation failed after {retries} attempts: {err}"
                        )
                        raise
                    jitter = random.uniform(0, 0.1 * current_delay)
                    sleep_time = current_delay + jitter
                    logger.warning(
                        f"Attempt {attempt}/{retries} failed ({err}). "
                        f"Retrying in {sleep_time:.2f}s..."
                    )
                    await asyncio.sleep(sleep_time)
                    current_delay *= backoff

        return wrapper

    return decorator
