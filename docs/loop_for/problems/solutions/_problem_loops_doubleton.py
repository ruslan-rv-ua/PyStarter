'''
"Дубльтон"

Будемо називати дубльтоном натуральне число, яке записується з використанням лише двох різних цифр.
Наприклад числа-дубльтони: 23, 35, 100, 12121.
Не дубльтони: 123, 9980.
Реалізуйте функцію next_doubleton(num).
Функція отримує натуральне число num.
Функція повертає найближче число-дубльтон більше за num.
'''
# ваш код починається тут

# https://www.codewars.com/kata/604287495a72ae00131685c7
def is_doubleton(num):
	digits = [0] * 10
	for ch in str(num):
		digits[int(ch)] = 1
	return sum(digits) == 2
	
def next_doubleton(num):
	while True:
		num += 1
		if is_doubleton(num):
			return num

# тут тести, не міняйте цей код
assert next_doubleton(120) == 121
assert next_doubleton(1234) == 1311
assert next_doubleton(10) == 12
assert next_doubleton(1) == 10
assert next_doubleton(111) == 112
