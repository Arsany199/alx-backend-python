#!/usr/bin/env python3
"""model for the basics of async"""

from asyncio import run
from time import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measure the runtime of wait_n execution"""
    start = time()

    run(wait_n(n, max_delay))

    end = time()

    return ((end - start) / n)
