'''
"Усі числа разом"

Реалізуйте функцію join_numbers_from_range()
яка об'єднує усі числа з діапазону у символьний рядок.
Числа одне від одного мають бути розділені одним пробілом.
Якщо діапазон пустий, функція повертає пустий рядок.
Діапазон задається двома числами:
	початкове значення from_inclusive, включається у діапазон.
	кінцеве значення to_exclusive, не включається у діапазон.
Якщо from_inclusive >= to_exclusive, діапазон вважати пустим.
'''
def join_numbers_from_range(from_inclusive, to_exclusive):
	# ваш код починається тут
	result = ''
	number = from_inclusive
	while number < to_exclusive:
		result += str(number) + ' '
		number += 1
	return result[:-1]
	
# далі тести, не чіпати!
assert join_numbers_from_range(1, 0) == ''
assert join_numbers_from_range(1, 1) == ''
assert join_numbers_from_range(-2, -1) == '-2'
assert join_numbers_from_range(-2, -2) == ''
assert join_numbers_from_range(1, 2) == '1'
assert join_numbers_from_range(2, 4) == '2 3'
assert join_numbers_from_range(5, 12) == '5 6 7 8 9 10 11'
assert join_numbers_from_range(-5, 0) == '-5 -4 -3 -2 -1'