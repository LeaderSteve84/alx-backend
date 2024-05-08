#!/usr/bin/python3
"""FIFO cache module"""
from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """FIFO Cache"""

    def __init__(self):
        """object constructor"""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """Assigne a key to a value"""
        if key is None or item is None:
            return

        if key not in self.stack:
            self.stack.append(key)
        else:
            self.migrate_to_last(key)

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard_d = self.stack[0]
            if discard_d:
                self.stack.remove(discard_d)
                del self.cache_data[discard_d]
                print("DISCARD: {}". format(discard_d))

    def get(self, key):
        """returns value in self.cache_dat linked to key"""
        return self.cache_data(key, None)

    def migrate_to_last(self, key):
        """move an element"""
        if self.stack[-1] != key:
            self.stack.remove(key)
            self.stack.append(key)
