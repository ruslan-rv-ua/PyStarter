import io
import unittest
from unittest.mock import patch

from .printer import (
    Printer,  # Assuming printer.py is in the same directory or accessible via PYTHONPATH
)


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


if __name__ == "__main__":
    unittest.main()
