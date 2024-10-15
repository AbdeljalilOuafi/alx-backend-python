#!/usr/bin/env python3
"""0-basic_async module"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously wait for a random delay between 0 and max_delay seconds.

    Args:
        max_delay (int): The maximum delay time in seconds (default is 10).

    Returns:
        float: The actual delay time waited.

    Raises:
        ValueError: If max_delay is negative.
    """
    random_value = random.uniform(0, max_delay)
    await asyncio.sleep(random_value)
    return random_value
