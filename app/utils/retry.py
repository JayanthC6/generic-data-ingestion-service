import asyncio
from functools import wraps


def retry(max_attempts=3, delay=2):
    """
    Retry decorator for async functions.
    """

    def decorator(func):

        @wraps(func)
        async def wrapper(*args, **kwargs):

            last_exception = None

            for attempt in range(1, max_attempts + 1):

                try:
                    return await func(*args, **kwargs)

                except Exception as e:

                    last_exception = e

                    print(
                        f"[Retry] Attempt {attempt}/{max_attempts} failed: {e}"
                    )

                    if attempt < max_attempts:
                        await asyncio.sleep(delay)

            raise last_exception

        return wrapper

    return decorator