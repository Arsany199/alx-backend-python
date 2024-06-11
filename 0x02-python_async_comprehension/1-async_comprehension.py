#!/usr/bin/env python3
"""model of async_comprehension"""

import asyncio
import random
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """function that generate list of 10 numbers between 0 and 10"""
    return [i async for i in async_generator()]
