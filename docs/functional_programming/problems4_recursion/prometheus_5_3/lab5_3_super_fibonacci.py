"""Супер Фібоначі.

Розробити функцію super_fibonacci(n, m),
яка приймає 2 аргументи -- додатні цілі числа n та m (0 < n, m <= 35),
та повертає число -- n-й елемент послідовності супер-Фібоначчі порядку m.

Нагадуємо, що послідовність Фібоначчі -- це послідовність чисел, в якій кожний елемент дорівнює сумі двох попередніх. Послідовністю супер-Фібоначчі порядку m будемо вважати таку послідовність чисел, в якій кожний елемент дорівнює сумі m попередніх. Перші m елементів (з порядковими номерами від 1 до m) вважатимемо одиницями.

Наприклад
Виклик функції: super_fibonacci(2, 1)
Повертає: 1
Виклик функції: super_fibonacci(3, 5)
Повертає: 1
Виклик функції: super_fibonacci(8, 2)
Повертає: 21
Виклик функції: super_fibonacci(9, 3)
Повертає: 57
"""
def super_fibonacci(n, m):
	if n <= m:
		return 1
	res = 0
	for last_index in range(1, m+1):
		last = super_fibonacci(n-last_index, m)
		res += last
	return res

# tests
assert super_fibonacci(2, 1) == 1
assert super_fibonacci(3, 5) == 1
assert super_fibonacci(8, 2) == 21
assert super_fibonacci(9, 3) == 57

assert super_fibonacci(10, 1) == 1
assert super_fibonacci(3, 5) == 1
assert super_fibonacci(17, 2) == 1597
assert super_fibonacci(24, 12) == 22529
assert super_fibonacci(35, 17) == 2097153
