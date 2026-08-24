from typing import List

class LRUCache:
    def __init__(self, capacity: int):
        self.LRU = {}
        self.queue = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.LRU:
            return -1
        self.queue.remove(key)
        self.queue.append(key)
        return self.LRU[key]

    def put(self, key: int, value: int) -> None:
        if key in self.LRU:
            self.LRU[key] = value
            self.queue.remove(key)
            self.queue.append(key)
            return
        if len(self.queue) == self.capacity:
            lru_key = self.queue.pop(0)
            del self.LRU[lru_key]
        self.queue.append(key)
        self.LRU[key] = value