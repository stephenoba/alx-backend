#!/usr/bin/python3
"""LIFO Queue-based policy
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Implementation of the LIFO queue policy"""
    def put(self, key, item):
        """Put method
        """
        if not key or not item:
            return
        if (key not in self.cache_data
                and len(self.cache_data) >= BaseCaching.MAX_ITEMS):
            last_in = self.cache_data.popitem()[0]
            print("DISCARD: {}".format(last_in))
        if key in self.cache_data:
            del self.cache_data[key]
        self.cache_data[key] = item

    def get(self, key):
        """Get Method
        """
        if (not key) or (key not in self.cache_data):
            return None
        return self.cache_data[key]
