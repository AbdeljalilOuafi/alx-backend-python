#!/usr/bin/env python3
"""8-make_multiplier module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Func doc"""

    def mult(m: float) -> float:
        """Func doc"""
        return m * multiplier

    return mult
