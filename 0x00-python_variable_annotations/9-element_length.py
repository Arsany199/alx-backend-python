#!/usr/bin/env python3
"""model return values with the appropriate types"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Computes the length of a list of sequences"""
    return [(i, len(i)) for i in lst]
