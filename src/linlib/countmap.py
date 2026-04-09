from typing import Any, Callable

class CountMap:
    def __init__(self, map: dict[Any, int] | None = None):
        if map is None:
            self._map = {}
        else:
            self._map = map

    def addIfAbsent(self, item) -> bool:
        absent = self._map.get(item) is None
        if absent:
            self._map[item] = 0
        return absent

    def insert(self, item, count: int):
        self.addIfAbsent(item)
        self._map[item] += count

    def remove(self, item, count: int):
        self.addIfAbsent(item)
        self._map[item] -= count

    def increment(self, item):
        self.insert(item, 1)

    def decrement(self, item):
        self.remove(item, 1)

    def forEach(self, callback: Callable):
        for key, value in self._map.items():
            callback(key, value)
