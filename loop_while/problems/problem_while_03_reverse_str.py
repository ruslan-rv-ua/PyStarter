'''
"Переверни рядок"

Реалізуйте функцію reverse_string()
яка приймає символьний рядок, а повертає його написаним задом наперед.
Не використовуйте зрізання.
'''
def reverse_string(string):
	# ваш код починається тут
	result = ''
	i = len(string) - 1
	while i >= 0:
		result += string[i]
		i -= 1
	return result
	
# далі тести, не чіпати!
assert reverse_string('123') == '321'
assert reverse_string('12') == '21'
assert reverse_string('1') == '1'
assert reverse_string('') == ''