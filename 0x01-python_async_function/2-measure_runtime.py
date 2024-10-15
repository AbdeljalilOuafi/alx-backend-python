#!/usr/bin/env python3
"""2-measure_runtime module"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n (n times with the specified
    max_delay).

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay of wait_random.

    Returns:
        float: The total execution time for wait_n in seconds.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    return float(total_time / n)
