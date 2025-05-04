import logging
import time
import asyncio
import functools
import inspect

logger = logging.getLogger(__name__)


def throttle(min_interval):
    def decorator(func):
        last_call = [0.0]  # Initialize with monotonic time's starting point

        if inspect.iscoroutinefunction(func):

            @functools.wraps(func)
            async def async_wrapper(*args, **kwargs):
                current_time = time.monotonic()
                elapsed = current_time - last_call[0]
                wait = min_interval - elapsed
                if wait > 0:
                    await asyncio.sleep(wait)
                result = await func(*args, **kwargs)
                last_call[0] = time.monotonic()  # Use monotonic time consistently
                return result

            return async_wrapper
        else:

            @functools.wraps(func)
            def sync_wrapper(*args, **kwargs):
                current_time = time.monotonic()
                elapsed = current_time - last_call[0]
                wait = min_interval - elapsed
                if wait > 0:
                    time.sleep(wait)
                result = func(*args, **kwargs)
                last_call[0] = time.monotonic()  # Use monotonic time consistently
                return result

            return sync_wrapper

    return decorator


def retry(
    max_retry=3,
    retry_interval=1,
    retry_on=None,
    retry_on_exception=None,
    log_level=logging.WARNING,
):
    """Decorator to add retry functionality (supports sync and async)"""
    def decorator(func):
        if inspect.iscoroutinefunction(func):

            @functools.wraps(func)
            async def async_wrapper(*args, **kwargs):
                for i in range(max_retry):
                    try:
                        res = await func(*args, **kwargs)
                        return res
                    except Exception as e:
                        if retry_on and not retry_on(e):
                            # If the exception is not matched by retry_on, re-raise it
                            raise e
                        if retry_on_exception and retry_on_exception(e):
                            # If exception matches retry_on_exception, re-raise it
                            raise e
                        if i + 1 == max_retry:
                            # If this is the last retry attempt, raise the exception
                            raise e
                        # Log the error and retry
                        logger.log(
                            log_level,
                            f"An error occurred while executing {func.__name__}",
                            exc_info=e,
                        )
                        logger.info(
                            f"Retry {i+1}/{max_retry} in {retry_interval} seconds"
                        )
                        await asyncio.sleep(retry_interval)

            return async_wrapper
        else:

            @functools.wraps(func)
            def sync_wrapper(*args, **kwargs):
                for i in range(max_retry):
                    try:
                        res = func(*args, **kwargs)
                        return res
                    except Exception as e:
                        if retry_on and not retry_on(e):
                            raise e
                        if retry_on_exception and retry_on_exception(e):
                            raise e
                        if i + 1 == max_retry:
                            raise e
                        logger.log(
                            log_level,
                            f"An error occurred while executing {func.__name__}",
                            exc_info=e,
                        )
                        logger.info(
                            f"Retry {i+1}/{max_retry} in {retry_interval} seconds"
                        )
                        time.sleep(retry_interval)

            return sync_wrapper

    return decorator


