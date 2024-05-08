#!/usr/bin/env python3
"""BasicCache"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Class of BasicCache"""

    def put(self, key, item):
        """assign to the dictionary.
        Args:
            key: key of dictionary
            item: Value of dictionary
        Returns:  updated dictionary self.cache_date..
        """

        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        assign to the dictionary.
        Args:
            key: key of dictionary
            item: Value of dictionary
        Returns:  value in self.cache_data linked to key.
            If key is None or if the key doesn’t exist in
            self.cache_data, return None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
