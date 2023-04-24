#!/usr/bin/env python3
"""string and int/float annotation"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    to_kv() takes k as str, v as union of int or float
    and returns a tuple of str and float.
    """
    sqr = v ** 2
    return (k, sqr)
