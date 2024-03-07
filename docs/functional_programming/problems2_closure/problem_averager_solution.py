"""
1. Вивчіть наступний код написаний в об'єктно-орієнтованому стилі.
2. У коментарях опишіть, що саме реалізовано.
3. Перепишіть код в функційному стилі.
Залишити лише ваше пояснення, ваш код та юніт-тесты.
"""

class Averager:
    def __init__(self):
        self._count = 0
        self._total = 0

    def __call__(self, value):
        self._count += 1
        self._total += value
        return self._total / self._count


def Averager(): # noqa
    count = 0
    total = 0
    def __call__(value):
        nonlocal count, total
        count += 1
        total += value
        return total / count
    return __call__

# юніт-тесты
a = Averager()
assert a(1) == 1.0
assert a(2) == 1.5
assert a(3) == 2.0
assert a(4) == 2.5
assert a(5) == 3.0
assert a(6) == 3.5
assert a(7) == 4.0
assert a(8) == 4.5
assert a(9) == 5.0
assert a(10) == 5.5
