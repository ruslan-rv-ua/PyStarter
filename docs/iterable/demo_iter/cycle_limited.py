class Cycle:
    def __init__(self, iterable, count):
        self._count = count
        self._items = list(iterable)
        self._index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        self._count -= 1
        if self._count < 0:
            raise StopIteration
        item = self._items[self._index]
        self._index = (self._index + 1) % len(self._items)
        return item
    
for i in Cycle(range(3), 5):
    print(i)

l = list(Cycle('123', 5))