# ваш код починається тут з наступного рядка.

'''"Арабські в римські"

Реалізуйте функцію int_to_roman.
Функція приймає ціле число у діапазоні від 0 до 3999 включно.
Функція повертає символьний рядок з римським представленням вхідного числа.
Тести з невалідними вхідними даними не проводяться.
'''
# не міняйте наступний код, це тести
assert int_to_roman(1) == 'I'
assert int_to_roman(59) == 'LIX'
assert int_to_roman(95) == 'XCV'
assert int_to_roman(98) == 'XCVIII'
assert int_to_roman(99) == 'XCIX'
assert int_to_roman(1950) == 'MCML'
assert int_to_roman(2021) == 'MMXXI'
assert int_to_roman(3000) == 'MMM'
assert int_to_roman(3999) == 'MMMCMXCIX'
