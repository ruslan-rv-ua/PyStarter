from numbers import Integral

ROMAN_BY_INT = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
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


class RomanInt(int):
    def __init__(self, value: int | str) -> None:
        print(value)
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, int):
            value = value
        elif isinstance(value, str):
            value = self.roman_to_int(value)
        else:
            raise TypeError("value must be an integer or a string")

        if value < 0 or value > 3999:
            raise ValueError("value must be between 0 and 3999")
        self._value = value

    def __repr__(self):
        return f"RomanInt({self.value})"

    def __str__(self) -> str:
        return self.int_to_roman(self.value)

    @staticmethod
    def roman_to_int(roman: str) -> int:
        result = 0
        old_int_ = 0
        for roman_num in reversed(roman):
            int_ = ROMAN_BY_INT[roman_num]
            if int_ < old_int_:
                result -= int_
            else:
                result += int_
            old_int_ = int_
        return result

    @staticmethod
    def int_to_roman(n: int) -> str:
        result = ""
        for int_, roman_num in ROMAN_BY_INT.items():
            while n >= int_:
                result += roman_num
                n -= int_
        return result

n1 = RomanInt(1)
n2 = RomanInt('I')
r = n1 + n2