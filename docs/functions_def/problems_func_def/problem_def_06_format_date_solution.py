'''
"Форматування дат"

Реалізуйте функцію get_formatted_date(), яка приймає на вхід три цілих числа:
день, місяць та рік,
а повертає їх як символьний рядок у відформатованому вигляді,
наприклад: 1953-02-30.
День і місяць треба форматувати так, щоб за необхідності додавався 0 зліва.
Наприклад, якщо у якості місяця прийшло число 7,
то у вихідному рядку вона має бути представлена як 07.
Рік треба форматувати так, щоб у вихідному рядку він доповнювався нулями з початку щоб вийшло 4 символи.
Наприклад, 0012.
'''
# ваш код починається тут
def format_number(number, positions):
	num_as_str = str(number)
	return '0' * (positions - len(num_as_str)) + num_as_str
	
def get_formatted_date(day, month, year):
	result = format_number(year, 4) + '-' + \
		format_number(month, 2) + '-' + \
		format_number(day, 2)
	return result

# не міняйте наступний код
assert get_formatted_date(30, 2, 1953) == '1953-02-30'
assert get_formatted_date(30, 12, 1953) == '1953-12-30'
assert get_formatted_date(3, 2, 1953) == '1953-02-03'
assert get_formatted_date(1, 1, 1) == '0001-01-01'
assert get_formatted_date(1, 1, 101) == '0101-01-01'