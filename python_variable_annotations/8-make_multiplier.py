#!/usr/bin/env python3
"Complex types - functions"
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """a type-annotated function make_multiplier that takes
    a float multiplier as argument
    and returns a function that multiplies a float by multiplier"""
    def multilpy(x: float) -> float:
        return x * multiplier
    return multilpy
