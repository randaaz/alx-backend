#!/usr/bin/env python3
'''
    This module provides a Server class to paginate
    a dataset of popular baby names.
'''
import csv
import math
from typing import List


def index_range(page, page_size):
    '''
        Calculate the start and end indexes for the pagination of a dataset.
    '''
    start = (page - 1) * page_size
    end = page * page_size
    return start, end


class Server:
    """ Server class to paginate a dataset of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:  # sourcery skip: identity-comprehension
        """ Load and cache the dataset from the CSV file.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
            Get a page from the dataset.
        '''
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        self.dataset()

        if self.dataset() is None:
            return []

        indexRange = index_range(page, page_size)
        return self.dataset()[indexRange[0]:indexRange[1]]
