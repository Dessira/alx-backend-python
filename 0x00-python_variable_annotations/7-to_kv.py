#!/usr/bin/env python3
"""type-annotated function to_kv"""
from typing import Union,  List, Tuple


def to_kv(k: str, v: List[Union[int, float]]) -> Tuple[str, float]:
    """string k and an int OR float v and returns a tuple"""
    return (k, v ** 2)
