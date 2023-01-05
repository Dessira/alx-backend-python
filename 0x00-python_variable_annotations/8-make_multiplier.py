#!/usr/bin/env python3
"""type-annotated function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ returns a function that multiplies a float by multiplier"""
    def multi(val: float) -> float:
        """Returns product of multiplier and val"""
        return val * multiplier
    return multi
