ROMAN_BY_INT = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


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
