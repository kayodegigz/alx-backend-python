#!/usr/bin/env python3
"""Duck Typing"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    safe_first_element Retrieves the first element of a sequence if present.
    """
    if lst:
        return lst[0]
    else:
        return None
