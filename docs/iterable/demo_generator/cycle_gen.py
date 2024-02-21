class Cycle:
    def __init__(self, iterable):
        self._iterable = iterable

    def __iter__(self):
        return self.infinite_iterator()
    
    def infinite_iterator(self):
        while True:
            yield from self._iterable

for c in Cycle([11,22,33]):
    print(c)
