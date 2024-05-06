#!/usr/bin/env python3
"""module of a pagination project"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ takes two integer arguments page and page_size.

    Args:
        page (int): page
        page_size (int): page size
    return: a list for those particular pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
