#!/usr/bin/env python3
"""model multiply a float"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float by multiplier"""
    return lambda number: multiplier * number
