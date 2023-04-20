#!/usr/bin/env python3
"""
Implement a method named get_page
"""
import csv
import math
from typing import List, Tuple, Dict


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
        """
        Paginate dataset
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start_idx, end_idx = index_range(page, page_size)
        return self.dataset()[start_idx:end_idx]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Get page with extra details

        Args
        ----
        page(int): Page number
        page_size(int): Size of page

        Returns
        -------
        A dict containing dataset and extra details
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        page_size = len(data)
        res = {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': page + 1 if total_pages > page else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
        return res
