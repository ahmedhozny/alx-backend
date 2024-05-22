#!/usr/bin/env python3
"""
MRUCache Module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class
    This class implements an MRU (Most Recently Used) caching system.
    """
    def __init__(self):
        """
        Initialize the FifoCache instance.
        """
        super().__init__()
        self.mru = []

    def put(self, key, item):
        """
        Add an item to the cache.
        """
        if not key or not item:
            return
        if key not in self.mru and len(self.mru) >= self.MAX_ITEMS:
            removed = self.mru.pop(0)
            self.cache_data.pop(removed)
            print("DISCARD: {}".format(removed))
        if key in self.mru:
            self.mru.remove(key)
        self.cache_data[key] = item
        self.mru.insert(0, key)

    def get(self, key):
        """
        Retrieve an item from the cache by key.
        """
        if not key:
            return None
        res = self.cache_data.get(key)

        if res is not None:
            self.mru.remove(key)
            self.mru.insert(0, key)
        return res
