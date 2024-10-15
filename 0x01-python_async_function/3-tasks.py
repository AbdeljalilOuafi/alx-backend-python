#!/usr/bin/env python3
"""3-tasks module"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns a task that waits for a random delay between 0 and
    max_delay (inclusive) seconds.

    Args:
        max_delay (int): The maximum delay time in seconds.

    Returns:
        asyncio.Task: The task that waits for the random delay.
    """
    return asyncio.create_task(wait_random(max_delay))
