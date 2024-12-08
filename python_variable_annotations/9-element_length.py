#!/usr/bin/env python3
" Let's duck type an iterable object"
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """a type-annotated function element_length that takes
       an iterable of sequences as input
       and returns a list of tuples:
       Each tuple contains a sequence from the input iterable
       and its corresponding length."""
    return [(i, len(i)) for i in lst]
