#!/usr/bin/env python3
"""type-annotated function sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns sum of an input list"""
    total: float = 0
    for i in input_list:
        total += i
    return total
