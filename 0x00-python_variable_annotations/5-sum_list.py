#!/usr/bin/env python3
"""model that sums a list of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """function sums a list of floats"""
    if input_list is None:
        return 0
    else:
        return float(sum(input_list))
