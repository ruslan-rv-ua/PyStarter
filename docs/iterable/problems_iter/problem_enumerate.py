"""Реалізуйте ітератор Enumerate, аналог вбудованого enumerate.
"""
from typing import Iterable

# unit tests
assert tuple(Enumerate("abc", 1)) == tuple(enumerate("abc", 1))
assert tuple(Enumerate("abc")) == tuple(enumerate("abc"))
assert list(Enumerate(range(10, 15), start=20)) == list(enumerate(range(10, 15), 20))
assert tuple(Enumerate(dict())) == tuple(enumerate(dict()))