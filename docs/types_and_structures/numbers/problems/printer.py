# ваш код починається тут, умова задачі далі
class Printer:
    def __lshift__(self, value):
        print(value)
        return self


"""Умова задачі
Реалізуйте клас `Printer`.
Цей клас повинен визначити оператор `<<` таким чином, щоб він друкував передане значення.
Оператор також повинен підтримувати ланцюжкове використання, дозволяючи друкувати кілька значень послідовно.

Приклад використання:
printer = Printer()
printer << 1
# Очікуваний вивід:
# 1

printer << 1.0
# Очікуваний вивід:
# 1.0

printer << "hello"
# Очікуваний вивід:
# hello

printer << "Hello" << "world"
# Очікуваний вивід:
# Hello
# world

printer << 2 << "+" << 2 << "=" << 2+2
# Очікуваний вивід:
# 2
# +
# 2
# =
# 4
"""


# юніт-тести, не міняйте цей код
import io  # noqa
import unittest  # noqa
from unittest.mock import patch  # noqa


class TestPrinter(unittest.TestCase):
    def test_print_integer(self):
        printer = Printer()
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            printer << 1
            self.assertEqual(mock_stdout.getvalue(), "1\n")

    def test_print_float(self):
        printer = Printer()
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            printer << 1.0
            self.assertEqual(mock_stdout.getvalue(), "1.0\n")

    def test_print_string(self):
        printer = Printer()
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            printer << "hello"
            self.assertEqual(mock_stdout.getvalue(), "hello\n")

    def test_print_chained_strings(self):
        printer = Printer()
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            printer << "Hello" << "world"
            self.assertEqual(mock_stdout.getvalue(), "Hello\nworld\n")

    def test_print_chained_mixed_types(self):
        printer = Printer()
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            printer << 2 << "+" << 2 << "=" << 2 + 2
            self.assertEqual(mock_stdout.getvalue(), "2\n+\n2\n=\n4\n")


if __name__ == "__main__":
    unittest.main(exit=False)
