from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        result = self.cache[key]
        return result

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


if __name__ == '__main__':
    #Example1
    # lRUCache = LRUCache(2)
    # lRUCache.put(1, 1)  # cache is {1=1}
    # lRUCache.put(2, 2)  # cache is {1=1, 2=2}
    # assert lRUCache.get(1) == 1    # return 1
    # lRUCache.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    # assert lRUCache.get(2) == -1    # returns -1 (not found)
    # lRUCache.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    # assert lRUCache.get(1) == -1    # return -1 (not found)
    # assert lRUCache.get(3) == 3    # return 3
    # assert lRUCache.get(4) == 4    # return 4

    cache = LRUCache(2)
    cache.put(2, 1)
    cache.put(1, 1)
    cache.put(2, 3)
    cache.put(4, 1)
    assert cache.get(1) == -1
    assert cache.get(2) == 3
