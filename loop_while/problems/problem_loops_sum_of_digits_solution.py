'''
"Сума цифр"

Реалізуйте функцію sum_of_digits().
Функція отримує число, повертає суму цифр цього числа.
'''

def sum_of_digits(number):
	# ваш код
	num_as_str = str(number)
	sum = 0
	index = 0
	while index < len(num_as_str):
		if num_as_str[index] in '0123456789':
			sum += int(num_as_str[index])
		index += 1
	return sum

assert sum_of_digits(0) == 0
assert sum_of_digits(1) == 1
assert sum_of_digits(5000005) == 10
assert sum_of_digits(-2) == 2
assert sum_of_digits(-2.3) == 5