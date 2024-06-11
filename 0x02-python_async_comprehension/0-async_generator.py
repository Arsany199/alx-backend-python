#!/usr/bin/env python3
"""model to generate loop in 10 no."""

from typing import Generator
import random
import asyncio


async def async_generator() -> Generator[float, None, None]:
    """function that yield async generator of 10 numbers"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
