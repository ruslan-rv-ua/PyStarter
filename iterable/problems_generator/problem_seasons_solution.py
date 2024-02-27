"""Реалізуйте клас, який представляє пори року (сезони): 
- зима (winter);
- весна (spring);
- літо (summer);
- осінь (fall).
Реалізуйте метод now(), який повертає поточний сезон (пору року).
Реалізуйте можливість ітеруватись по порам року вказавши початковий сезон і кількість сезонів.
Для юніттестів використовується модуль pytest.
Цей модуль треба встановити: 
pip install pytest
Результати тестування будуть у файлі test_results.txt.
"""

from enum import Enum, StrEnum
from datetime import date
from itertools import cycle, islice


class Seasons(str, Enum):
    def __str__(self) -> str:
        return self.value

    WINTER = "зима"
    SPRING = "весна"
    SUMMER = "літо"
    FALL = "осінь"

    @classmethod
    def iter(self, start: "Seasons", count: int):
        if not isinstance(start, Seasons):
            raise TypeError("start must be an instance of Seasons")
        if not isinstance(count, int):
            raise TypeError("count must be an instance of int")
        if count < 0:
            raise ValueError("count must be positive")
        
        seasons_iterator = cycle(Seasons)
        start_index = list(Seasons).index(start)
        yield from islice(seasons_iterator, start_index, start_index+count)

    @classmethod
    def now(self):
        month = date.today().month
        if month in {12, 1, 2}:
            return Seasons.WINTER
        elif month in {3, 4, 5}:
            return Seasons.SPRING
        elif month in {6, 7, 8}:
            return Seasons.SUMMER
        elif month in {9, 10, 11}:
            return Seasons.FALL



# юніт-тести, використовуйте як підказку
import pytest  # noqa
from contextlib import redirect_stdout  # noqa

try:
    from collections.abc import Iterator
except ImportError:
    from collections import Iterator


def test_iter_start_type():
    with pytest.raises(TypeError):
        list(Seasons.iter("зима", 5))
    with pytest.raises(TypeError):
        list(Seasons.iter(5, 5))


def test_iter_count_type():
    with pytest.raises(TypeError):
        list(Seasons.iter(Seasons.now(), 3.0))
    with pytest.raises(TypeError):
        list(Seasons.iter(Seasons.now(), None))


def test_iter_couont_negative():
    with pytest.raises(ValueError):
        list(Seasons.iter(Seasons.now(), -1))


def test_seasons():
    assert Seasons.FALL in Seasons


def test_season_str():
    assert str(Seasons.FALL) == "осінь"
    assert str(Seasons.WINTER) == "зима"


def test_now():
    assert Seasons.now() == Seasons.WINTER


def test_now_str():
    assert str(Seasons.now()) == "зима"


def test_iter_returns_iterator():
    resutl = Seasons.iter(Seasons.now(), 5)
    assert isinstance(resutl, Iterator)


def test_iter_5():
    assert (
        ", ".join(str(season) for season in Seasons.iter(Seasons.now(), 5))
        == "зима, весна, літо, осінь, зима"
    )


def test_iter_1():
    assert list(Seasons.iter(Seasons.now(), 1)) == ["зима"]


def test_iter_0():
    assert list(Seasons.iter(Seasons.now(), 0)) == []


pytest.main(["-q", __file__])
with open("test_results.txt", "w") as f, redirect_stdout(f):
    pytest.main(["-q", __file__])
