#!/usr/bin/env python3
"""FIFO cache module"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO Cache"""

    def __init__(self):
        """object constructor"""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """Assigne a key to a value"""
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard_d = self.stack.pop()
            del self.cache_data[discard_d]
            print("DISCARD: {}". format(discard_d))

        if key not in self.stack:
            self.stack.append(key)
        else:
            self.migrate_to_last(key)

    def get(self, key):
        """returns value in self.cache_dat linked to key"""
        if key is None or key not in self.cache_data.keys():
            return None

        return self.cache_data.get(key)

    def migrate_to_last(self, key):
        """move an element"""
        if self.stack[-1] != key:
            self.stack.remove(key)
            self.stack.append(key)
