#!/usr/bin/env python3
""" file basic cashe """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
        BaseCache class
    """

    def put(self, key, item):
        """
            put method
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
            get method
        """
        return self.cache_data.get(key, None)
