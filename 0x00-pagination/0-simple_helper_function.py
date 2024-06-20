#!/usr/bin/env python3
'''
    This module contains a function to calculate the
    start and end indexes for pagination.
'''


def index_range(page, page_size):
    '''
        Returns: tuple: A tuple containing the start and end indexes.
    '''
    start = (page - 1) * page_size
    end = page * page_size
    return start, end
