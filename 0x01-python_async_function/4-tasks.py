#!/usr/bin/env python3
"""4-tasks module"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
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
        delays.append(task_wait_random(max_delay))
    return sorted(await asyncio.gather(*delays))
