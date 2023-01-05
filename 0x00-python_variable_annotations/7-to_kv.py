#!/usr/bin/env python3
"""type-annotated function to_kv"""
from typing import Union,  List


def to_kv(k: str, v: List[Union[int, float]]) -> tuple:
    """string k and an int OR float v and returns a tuple"""
    return (k, v ** 2)
