#!/usr/bin/env python3
"""type-annotated function sum_mixed_list """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """returns sum of mxd_lst as float"""
    total: float = 0.0
    for i in mxd_lst:
        total += i
    return total
