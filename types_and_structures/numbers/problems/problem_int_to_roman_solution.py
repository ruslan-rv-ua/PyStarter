# тут ваш код, умова задачі далі
ROMAN_BY_INT = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I",
}


def int_to_roman(n: int) -> str:
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 1 or n > 3999:
        raise ValueError("Input must be in the range 1 to 3999")
    
    result = ""
    for int_, roman_num in ROMAN_BY_INT.items():
        while n >= int_:
            result += roman_num
            n -= int_
    return result


'''"Арабські в римські"

Римська система числення:
http://ruslan.rv.ua/PyStarter/types_and_structures/numbers/roman_numerals.html
Реалізуйте функцію int_to_roman.
Функція повертає символьний рядок з римським представленням вхідного числа.
'''

# не міняйте наступний код, це тести
import unittest

class TestIntToRoman(unittest.TestCase):
    def test_int_to_roman(self):
        self.assertEqual(int_to_roman(1), 'I')
        self.assertEqual(int_to_roman(59), 'LIX')
        self.assertEqual(int_to_roman(95), 'XCV')
        self.assertEqual(int_to_roman(98), 'XCVIII')
        self.assertEqual(int_to_roman(99), 'XCIX')
        self.assertEqual(int_to_roman(1950), 'MCML')
        self.assertEqual(int_to_roman(2021), 'MMXXI')
        self.assertEqual(int_to_roman(3000), 'MMM')
        self.assertEqual(int_to_roman(3999), 'MMMCMXCIX')

    def test_input_type(self):
        with self.assertRaises(TypeError):
            int_to_roman("a") # type: ignore

    def test_input_value_too_low(self):
        with self.assertRaises(ValueError):
            int_to_roman(0)

    def test_input_value_too_high(self):
        with self.assertRaises(ValueError):
            int_to_roman(4000)

if __name__ == '__main__':
    unittest.main(exit=False)
