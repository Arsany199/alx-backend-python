#!/usr/bin/env python3
"""model for the basics of synic"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait random n times"""
    wait_t = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    return [await tasks for tasks in asyncio.as_completed(wait_t)]
