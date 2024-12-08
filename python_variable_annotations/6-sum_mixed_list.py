#!/usr/bin/env python3
"Complex types - mixed list"
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[float, int]]) -> float:
    """a type-annotated function sum_mixed_list
    which takes a list mxd_lst of integers and floats
    and returns their sum as a float."""
    return sum(mxd_list)
