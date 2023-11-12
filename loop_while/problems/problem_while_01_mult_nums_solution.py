'''
"Перемнож"

Реалізуйте функцію multiply_numbers_from_range()
яка перемножує усі числа з діапазону.
Якщо діапазон пустий, функція повертає 0.
Діапазон задається двома числами:
	початкове значення from_inclusive, включається у діапазон.
	кінцеве значення to_exclusive, не включається у діапазон.
Якщо from_inclusive >= to_exclusive, діапазон вважати пустим.
'''
def multiply_numbers_from_range(from_inclusive, to_exclusive):
	# ваш код починається тут
	if to_exclusive <= from_inclusive:
		return 0
	result = 1
	number = from_inclusive
	while number < to_exclusive:
		result *= number
		number += 1
	return result
	
# далі тести, не чіпати!
assert multiply_numbers_from_range(1, 6) == 120
assert multiply_numbers_from_range(2, 4) == 6
assert multiply_numbers_from_range(2, 3) == 2
assert multiply_numbers_from_range(6, 6) == 0
assert multiply_numbers_from_range(6, 5) == 0