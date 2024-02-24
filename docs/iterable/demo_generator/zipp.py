class Zip:
    def __init__(self, *iterables):
        self._iterators = [iter(ite) for ite in iterables]
    def __iter__(self):
        return self.iterator()
    def iterator(self):
        while True:
            try:
                result = [next(iterator) for iterator in self._iterators]
            except StopIteration:
                return
            yield tuple(result)


for t in Zip('abc', [1,2,3], range(5)):
    print(t)