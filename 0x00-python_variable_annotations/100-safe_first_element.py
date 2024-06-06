#!/usr/bin/env python3
"""model that Augment code with the correct duck-typed annotations"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """get the first element from lst"""
    if lst:
        return (lst[0])
    else:
        return None
