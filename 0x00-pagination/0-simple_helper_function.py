#!/usr/bin/env python3
"""
Pagination helper
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Pagination helper function
    """
    return (page - 1) * page_size, page * page_size
