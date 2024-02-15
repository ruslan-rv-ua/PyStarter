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
    result = ""
    for int_, roman_num in ROMAN_BY_INT.items():
        while n >= int_:
            result += roman_num
            n -= int_
    return result


""""Арабські в римські"

Реалізуйте функцію int_to_roman.
Функція приймає ціле число у діапазоні від 0 до 3999 включно.
Функція повертає символьний рядок з римським представленням вхідного числа.
"""
# не міняйте наступний код, це тести
assert int_to_roman(1) == "I"
assert int_to_roman(59) == "LIX"
assert int_to_roman(95) == "XCV"
assert int_to_roman(98) == "XCVIII"
assert int_to_roman(99) == "XCIX"
assert int_to_roman(1950) == "MCML"
assert int_to_roman(2021) == "MMXXI"
assert int_to_roman(3000) == "MMM"
assert int_to_roman(3999) == "MMMCMXCIX"
