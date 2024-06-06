#!/usr/bin/env python3
"""model that sum mixed list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """function that take mixed list int, float and return float"""
    return (float(sum(mxd_lst)))
