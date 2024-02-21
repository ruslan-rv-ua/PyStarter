"""Реалізуйте ітератор Enumerate, аналог вбудованого enumerate.
Використовуййте підказки типів.
"""
from typing import Iterable


# unit tests
assert tuple(enumerate("abc", 1)) == tuple(enumerate("abc", 1))
assert tuple(enumerate("abc")) == tuple(enumerate("abc"))
assert list(enumerate(range(10, 15), start=20)) == list(enumerate(range(10, 15), 20))
