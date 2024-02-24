"""Реалізуйте клас, який представляє пори року (сезони): зима, весна, літо, осінь.
Реалізуйте метод now(), який повертає поточний сезон.
Реалізуйте можливість ітеруватись по порам року вказавши початковий сезон і кількість сезонів.
"""

from enum import Enum
from datetime import date


class Seasons(str, Enum):
    WINTER = "зима"
    SPRING = "весна"
    SUMMER = "літо"
    FALL = "осінь"

    @classmethod
    def iter(self, start: "Seasons", count: int):
        return SeasonsIterator(start, count)

    @classmethod
    def now(self):
        month = date.today().month
        if month in {12,1,2}:
            return Seasons.WINTER
        elif month in {3,4,5}:
            return Seasons.SPRING
        elif month in {6,7,8}:
            return Seasons.SUMMER
        elif month in {9,10,11}:
            return Seasons.FALL

    def __str__(self) -> str:
        return self.value


class SeasonsIterator:
    def __init__(self, start: Seasons, count: int):
        self._count = count
        self._seasons_list = list(Seasons)
        self._index = self._seasons_list.index(start)

    def __iter__(self):
        return self

    def __next__(self):
        self._count -= 1
        if self._count < 0:
            raise StopIteration
        item = self._seasons_list[self._index]
        self._index = (self._index + 1) % len(self._seasons_list)
        return item


# юніт-тест, він же єдина підказка
assert (
    ", ".join([str(season) for season in Seasons.iter(Seasons.now(), 5)])
    == "зима, весна, літо, осінь, зима"
)
assert list(Seasons.iter(Seasons.now(), 0)) == []