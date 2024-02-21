class Zip:

    def __init__(self, *iterables):
        self._iterables = iterables
        self._iterators = [iter(ite) for ite in iterables]

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return tuple(next(iterator) for iterator in self._iterators)
        except StopIteration:
            raise StopIteration