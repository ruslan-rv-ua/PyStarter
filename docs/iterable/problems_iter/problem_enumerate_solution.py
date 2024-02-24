"""Реалізуйте ітератор Enumerate, аналог вбудованого enumerate.
"""
from typing import Iterable


class Enumerate:
    def __init__(self, iterable: Iterable, start: int = 0):
        self._index = start - 1
        self._iterator = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        self._index += 1
        return (self._index, next(self._iterator))


# unit tests
assert tuple(Enumerate("abc", 1)) == tuple(enumerate("abc", 1))
assert tuple(Enumerate("abc")) == tuple(enumerate("abc"))
assert list(Enumerate(range(10, 15), start=20)) == list(enumerate(range(10, 15), 20))
assert tuple(Enumerate(dict())) == tuple(enumerate(dict()))