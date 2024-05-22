#!/usr/bin/env python3
"""
LIFOCache Module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class
    This class implements a LIFO (Last In, First Out) caching system.
    """
    def __init__(self):
        """
        Initialize the FifoCache instance.
        """
        super().__init__()
        self.lifo = []

    def put(self, key, item):
        """
        Add an item to the cache.
        """
        if not key or not item:
            return
        if key not in self.lifo and len(self.lifo) >= self.MAX_ITEMS:
            removed = self.lifo.pop(0)
            self.cache_data.pop(removed)
            print("DISCARD: {}".format(removed))
        if key in self.lifo:
            self.lifo.remove(key)
        self.cache_data[key] = item
        self.lifo.insert(0, key)

    def get(self, key):
        """
        Retrieve an item from the cache by key.
        """
        if not key:
            return None
        return self.cache_data.get(key)
