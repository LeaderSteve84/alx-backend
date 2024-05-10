#!/usr/bin/env python3
"""LFU cache module"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    A class that represents a cache with least
    recently used (LFU) strategy.

    Attributes:
        cache_data (dict): The cache data stored
        as a key-value pairs.
        stack (list): A list that stores the keys
        in the order of their usage.
    """

    def __init__(self):
        """object constructor"""
        super().__init__()
        self.stack = []
        self.stackCount = {}

    def put(self, key, item):
        """Assign a key to a value"""
        if key is None or item is None:
            return

        self.cache_data[key] = item

        itemCount = self.stackCount.get(key, None)

        if itemCount is not None:
            self.stackCount[key] += 1
        else:
            self.stackCount[key] = 1

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard_d = self.stack.pop(0)
            del self.stackCount[discard_d]
            del self.cache_data[discard_d]
            print("DISCARD: {}". format(discard_d))

        if key not in self.stack:
            self.stack.insert(0, key)

        self.migrate_to_last(key)

    def get(self, key):
        """returns value in self.cache_dat linked to key"""
        val = self.cache_data.get(key, None)
        if val is not None:
            self.stackCount[key] += 1
            self.migrate_to_last(item=key)
        return val

    def migrate_to_last(self, item):
        """move an element"""
        length = len(self.stack)

        idexV = self.stack.index(item)
        itemCount = self.stackCount[item]

        for x in range(idexV, length):
            if x != (length - 1):
                nx = self.stack[x + 1]
                nxCount = self.stackCount[nx]

                if nxCount > itemCount:
                    break

        self.stack.insert(x + 1, item)
        self.stack.remove(item)
