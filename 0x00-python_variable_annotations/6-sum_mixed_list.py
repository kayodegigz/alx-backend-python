#!/usr/bin/env python3
"""Annotating a mixed list"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    function collects a list mixed with int and float
    """
    return sum(mxd_lst)
