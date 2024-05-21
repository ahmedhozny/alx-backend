#!/usr/bin/env python3
"""
pagination server module
"""
import csv
from typing import List, Tuple, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Pagination helper function
    """
    return (page - 1) * page_size, page * page_size


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
        """Get a page of data from the dataset.
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        end = min(len(data) - 1, end)
        if start > len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Get a page of data along with pagination information.
        """
        page_data = self.get_page(page, page_size)
        start, end = index_range(page, page_size)
        data = self.__dataset
        next_page = None if start + page_size > len(data) else page - 1
        prev_page = None if start - page_size < 0 else page - 1
        return dict(
            page_size=len(page_data),
            page=page,
            data=page_data,
            next_page=next_page,
            prev_page=prev_page,
            total_pages=(len(data) - 1) // page_size + 1
        )
