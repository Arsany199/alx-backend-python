#!/usr/bin/env python3
"""model that take string and int or float"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """function that take sting and int OR float and return tuple"""
    return (k, float(v ** 2))
