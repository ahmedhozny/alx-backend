#!/usr/bin/env python3
"""
LRUCache Module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class
    This class implements an LRU (Least Recently Used) caching system.
    """
    def __init__(self):
        """
        Initialize the FifoCache instance.
        """
        super().__init__()
        self.lru = []

    def put(self, key, item):
        """
        Add an item to the cache.
        """
        if not key or not item:
            return
        if key not in self.lru and len(self.lru) >= self.MAX_ITEMS:
            removed = self.lru.pop(0)
            self.cache_data.pop(removed)
            print("DISCARD: {}".format(removed))
        if key in self.lru:
            self.lru.remove(key)
        self.cache_data[key] = item
        self.lru.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache by key.
        """
        if not key:
            return None
        res = self.cache_data.get(key)

        if res is not None:
            self.lru.remove(key)
            self.lru.append(key)
        return res
