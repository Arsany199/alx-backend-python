#!/usr/bin/env python3
"""model basic of async"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """wait for a random number for seconds"""
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return (wait_time)
