#!/usr/bin/env python3
"""module for pagination project"""

from typing import Tuple, List, Dict, Any
import csv
import math


index_range = __import__("0-simple_helper_function").index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """takes two integer arguments page with default
        value 1 and page_size with default value 10
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        resultList = []

        if start >= len(self.dataset()):
            return resultList
        resultList = self.dataset()
        return resultList[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Returns an object"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        totalPages = int(len(self.dataset()) / page_size)
        nextPage = page + 1 if (page + 1) < totalPages else None
        prevPage = page - 1 if page > 1 else None

        return {
            "page_size": len(self.get_page(page, page_size)),
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": nextPage,
            "prev_page": prevPage,
            "total_pages": totalPages
        }
