#!/usr/bin/env python3
"""LRU cache module"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU Cache"""

    def __init__(self):
        """object constructor"""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """Assign a key to a value"""
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard_d = self.stack.pop(0)
            del self.cache_data[discard_d]
            print("DISCARD: {}". format(discard_d))

        if key not in self.stack:
            self.stack.append(key)
        else:
            self.migrate_to_last(key)

    def get(self, key):
        """returns value in self.cache_dat linked to key"""
        val = self.cache_data.get(key, None)
        if val is not None:
            self.migrate_to_last(key)
        return val

    def migrate_to_last(self, key):
        """move an element"""
        if self.stack[-1] != key:
            self.stack.remove(key)
            self.stack.append(key)
