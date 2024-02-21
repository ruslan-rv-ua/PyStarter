"""Реалізуйте клас, який представляє пори року (сезони): зима, весна, літо, осінь.
Реалізуйте метод now(), який повертає поточний сезон.
Реалізуйте можливість ітеруватись по порам року вказавши початковий сезон і кількість сезонів.
"""
import datetime
import itertools
class Seasons:
    seasons = ['зима', 'весна', 'літо', 'осінь']

    @staticmethod
    def now():
        # Assuming the current month defines the current season
        month = datetime.datetime.now().month
        if month in [12, 1, 2]:
            return 'зима'
        elif month in [3, 4, 5]:
            return 'весна'
        elif month in [6, 7, 8]:
            return 'літо'
        else:
            return 'осінь'

    @staticmethod
    def iter(start_season, num_seasons):
        start_index = Seasons.seasons.index(start_season)
        seasons_cycle = itertools.cycle(Seasons.seasons)
        # Move to the start_season
        for _ in range(start_index):
            next(seasons_cycle)
        # Yield the seasons
        for _ in range(num_seasons):
            yield next(seasons_cycle)

# юніт-тест, він же єдина підказка
assert (
    ", ".join([str(season) for season in Seasons.iter(Seasons.now(), 5)])
    == "зима, весна, літо, осінь, зима"
)
