from datetime import datetime

class Seasons:
    SEASONS = ["зима", "весна", "літо", "осінь"]
    WINTER = 0
    SPRING = 1
    SUMMER = 2
    FALL = 3

    @staticmethod
    def now():
        """Returns the current season"""
        now = datetime.now()
        if now.month in (12, 1, 2):
            return Seasons.WINTER
        elif now.month in (3, 4, 5):
            return Seasons.SPRING
        elif now.month in (6, 7, 8):
            return Seasons.SUMMER
        else:
            return Seasons.FALL

    @staticmethod
    def iter(start_season, count):
        """Iterates over the seasons starting from the given season
        and for the given number of seasons.
        """
        if not isinstance(start_season, int) or not isinstance(count, int):
            raise TypeError("Both start_season and count must be integers")
        if count < 0:
            raise ValueError("Count must be non-negative")
        if start_season < 0 or start_season >= len(Seasons.SEASONS):
            raise ValueError("Start season must be in the range [0, 3]")

        season_index = start_season
        for _ in range(count):
            yield Seasons.SEASONS[season_index]
            season_index = (season_index + 1) % len(Seasons.SEASONS)


# Run the tests
pytest.main(["-q", __file__])

# Save the test results to a file
with open("test_results.txt", "w") as f, redirect_stdout(f):
    pytest.main(["-q", __file__])