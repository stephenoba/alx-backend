#!/usr/bin/env python3
"""
Module contains function index_range
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Function that returns a tuple of size two containing a start
    index and an end index

    Args
    ----
    page(int): Page number
    page_size(int): Size of page

    Returns
    -------
    A tuple containing the start index and end index of the page
    """
    start_index = page_size * (page - 1)
    end_index = page * page_size
    return start_index, end_index
