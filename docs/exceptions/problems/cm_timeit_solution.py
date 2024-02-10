'''Реалізуйте контекст-менеджер `MeasureTime` який заміряє час виконання блока коду.
По закінченні виводить результат заокруглений до двох знаків у вигляді:
"Час виконання: 0.56 секунд"

Зверніть увагу на наступні функції з модуля time:
- monotonic()
- monotonic_ns()
- perf_counter()
- perf_counter_ns()
'''
# ваш код з наступного рядка

from time import monotonic

class MeasureTime:
    def __enter__(self):
        self.start_time = monotonic()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Час виконання: {monotonic() - self.start_time:.2f} секунд")

# Заміряємо 10 мільйонів ітерацій:
with MeasureTime() as t:
    for _ in range(10000000):
        pass
