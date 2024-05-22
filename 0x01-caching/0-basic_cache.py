#!/usr/bin/env python3
"""
BasicCache Module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class
    This class implements a basic caching system
    without any limit on the number of items stored.
    """
    def __init__(self):
        """
        Initialize the BasicCache instance.
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache.
        """
        if not key or not item:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache by key.
        """
        if not key:
            return None
        return self.cache_data.get(key)
