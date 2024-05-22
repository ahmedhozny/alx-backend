#!/usr/bin/env python3
"""
FIFOCache Module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FifoCache class
    This class implements a FIFO (First In, First Out) caching system.
    """
    def __init__(self):
        """
        Initialize the FifoCache instance.
        """
        super().__init__()
        self.fifo = []

    def put(self, key, item):
        """
        Add an item to the cache.
        """
        if not key or not item:
            return
        if key not in self.fifo and len(self.fifo) >= self.MAX_ITEMS:
            removed = self.fifo.pop(0)
            self.cache_data.pop(removed)
            print("DISCARD: {}".format(removed))
        if key in self.fifo:
            self.fifo.remove(key)
        self.cache_data[key] = item
        self.fifo.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache by key.
        """
        if not key:
            return None
        return self.cache_data.get(key)
