#!/usr/bin/python3
""" This module contains the LRUCache class that
inherits from BaseCaching. """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class """

    def __init__(self):
        """ Initialize the LRUCache. """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add an item in the cache. """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first = self.get_first_list(self.queue)
            if first:
                self.queue.pop(0)
                del self.cache_data[first]
                print("DISCARD: {}".format(first))

        if key not in self.queue:
            self.queue.append(key)
        else:
            self.mv_last_list(key)

    def get(self, key):
        """ Get an item by key. """
        item = self.cache_data.get(key, None)
        if item is not None:
            self.mv_last_list(key)
        return item

    def mv_last_list(self, item):
        """ Move an item to the end of the queue. """
        length = len(self.queue)
        if self.queue[length - 1] != item:
            self.queue.remove(item)
            self.queue.append(item)

    @staticmethod
    def get_first_list(array):
        """ Get the first item in the list. """
        return array[0] if array else None
