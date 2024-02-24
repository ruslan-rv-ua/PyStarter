class Fibonacci:
    def __init__(self, count):
        self._count = count
        self._a = 1
        self._b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._count == 0:
            raise StopIteration
        item = self._a
        self._a, self._b = self._b, self._a + self._b
        self._count -= 1
        return item

i=iter(Fibonacci(3))
