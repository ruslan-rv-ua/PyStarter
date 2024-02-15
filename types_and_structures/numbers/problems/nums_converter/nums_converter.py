# ваш код з наступного рядка
DIGITS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def convert_n_to_m(x, n, m):
	if isinstance(x, str):
		from_num = x.upper()
	elif isinstance(x, int):
		from_num = str(x).upper()
	else:
		return False
	
	if not all(ch in DIGITS[:n] for ch in from_num):
		return False
	
	decimal = 0
	for pow, digit in enumerate(from_num[::-1]):
		decimal += n**pow * DIGITS.index(digit)
	
	if m == 1:
		return DIGITS[0] * decimal
		
	to_num = ''
	while decimal:
		decimal, rest = divmod(decimal, m)
		to_num = DIGITS[rest] + to_num
	return to_num if to_num else DIGITS[0]


'''
Розробити функцію convert_n_to_m(x, n, m),
яка приймає 3 аргументи -- ціле число (в системі числення з основою n) або рядок x, що представляє таке число, та цілі числа n та m (1 <= n, m <= 36),
та повертає рядок -- представлення числа х у системі числення m.

У випадку, якщо аргумент х не є числом або рядком, або не може бути представленням цілого невід'ємного числа в системі числення з основою n, повернути логічну константу False.

В системах числення з основою більше десяти для позначення розрядів із значенням більше 9 використовувати літери латинського алфавіту у верхньому регістрі від A до Z. У вхідному x можуть використовуватися обидва регістри.

Вважати, що в одиничній системі числення число записується відповідною кількістю нулів.

Наприклад
Виклик функції: convert_n_to_m([123], 4, 3)
Повертає: False
Виклик функції: convert_n_to_m("0123", 5, 6)
Повертає: 102
Виклик функції: convert_n_to_m("123", 3, 5)
Повертає: False
Виклик функції: convert_n_to_m(123, 4, 1)
Повертає: 000000000000000000000000000
Виклик функції: convert_n_to_m(-123.0, 11, 16)
Повертає: False
Виклик функції: convert_n_to_m("A1Z", 36, 16)
Повертає: 32E7
'''

		
# тести
assert convert_n_to_m([123], 4, 3) == False
assert convert_n_to_m("0123", 5, 6) == '102'
assert convert_n_to_m("123", 3, 5) == False
assert convert_n_to_m(123, 4, 1) == '000000000000000000000000000'
assert convert_n_to_m(-123.0, 11, 16) == False
assert convert_n_to_m("A1Z", 36, 16) == '32E7'

assert convert_n_to_m([1], 2, 2) == False
assert convert_n_to_m(True, 1, 2) == False
assert convert_n_to_m({1: 0}, 2, 2) == False
assert convert_n_to_m(-777, 10, 2) == False
assert convert_n_to_m(123123123123123123123.0, 11, 16) == False
assert convert_n_to_m(100, 2, 1) == '0000'
assert convert_n_to_m(0, 10, 2) == '0'
assert convert_n_to_m(000, 10, 2) == '0'
assert convert_n_to_m(777, 10, 2) == '1100001001'
assert convert_n_to_m('000', 10, 2) == '0'
assert convert_n_to_m('ZZZZ', 36, 13) == '46A672'
assert convert_n_to_m('000ZZZZ', 36, 13) == '46A672'
assert convert_n_to_m('ZZZZ', 35, 13) == False
assert convert_n_to_m('qweasd', 33, 36) == 'HGPEYJ'
assert convert_n_to_m('123123123123123123123', 11, 16) == '2C09BC518E8048D23A'
assert convert_n_to_m(123123123123123123123, 11, 16) == '2C09BC518E8048D23A'
assert convert_n_to_m(123123123123123123123, 10, 10) == '123123123123123123123'
assert convert_n_to_m('bnh34521', 31, 14) == '119337DC2BC'
assert convert_n_to_m('bnh34521', 11, 14) == False
