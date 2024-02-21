class Cycle:
    def __init__(self, iterable):
        self._items = list(iterable)
        self._index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        item = self._items[self._index]
        self._index = (self._index + 1) % len(self._items)
        return item
    
i = Cycle('abc')
for _ in range(10):
    print(next(i))
