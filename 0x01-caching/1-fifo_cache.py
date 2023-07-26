#!/usr/bin/python3
"""FIFO Queue-based policy
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Implementation of the FIFO queue policy"""
    def put(self, key, item):
        """Put method
        """
        if not key or not item:
            return
        if (key not in self.cache_data
                and len(self.cache_data) >= BaseCaching.MAX_ITEMS):
            first_in = list(self.cache_data.keys())[0]
            self.cache_data.pop(first_in)
            print("DISCARD: {}".format(first_in))
        self.cache_data[key] = item

    def get(self, key):
        """Get Method
        """
        if (not key) or (key not in self.cache_data):
            return None
        return self.cache_data[key]
