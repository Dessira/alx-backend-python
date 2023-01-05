#!/usr/bin/env python3
"""Annotate the below function’s parameters"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns list length"""
    return [(i, len(i)) for i in lst]
