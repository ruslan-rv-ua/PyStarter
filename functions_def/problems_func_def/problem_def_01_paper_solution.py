'''
"Скласти аркуш паперу"

Реалізуйте функцію num_layers(n)
яка буде повертати товщину аркуша паперу у метрах після складання цього аркуша n раз.
Товщина нескладеного аркуша — 0.5 міліметра.
Приклади:
num_layers(1) → 0.001
# Аркуш паперу, складений 1 раз, має товщину 1 міліметр або 0.001 метра
num_layers(4) → 0.008
num_layers(21) → 1048.576
'''
SHEET_THICKNESS = 0.0005 # in meters

def num_layers(n):
	# ваш код починається тут
	return SHEET_THICKNESS * 2 ** n
# не міняйте наступний код
assert num_layers(0) == 0.0005
assert num_layers(1) == 0.001
assert num_layers(4) == 0.008
assert num_layers(21) == 1048.576
