#!/usr/bin/env python3
"""model calculate the time of 4 comprehensions"""

import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """function calculate the time to execute 4 parallel comprhentions"""
    start = time.time()
    exc = [async_comprehension() for i in range(4)]
    await asyncio.gather(*exc)
    end = time.time()

    return (end - start)
