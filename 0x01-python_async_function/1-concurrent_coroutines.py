#!/usr/bin/env python3
"""1-concurrent_coroutines module"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay of wait_random.

    Returns:
        List[float]: List of all the delays (float values).
    """
    delays = []
    for _ in range(n):
        delays.append(asyncio.create_task(wait_random(max_delay)))
    return sorted(await asyncio.gather(*delays))
