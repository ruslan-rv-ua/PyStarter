'''
"Sort and strip"

Реалізуйте функцію sort_and_strip().
Функція приймає непустий кортеж чисел, усі елементи цього кортежа унікальні (мають різні значення).
Якщо кількість елементів у переданому кортежі меньше 3, функція повертає None.
В інших випадках функція повертає переданий їй кортеж,
але відсортований за зростанням і без мінімального і максимального елементів.
'''
# ваш код починається тут
def sort_and_strip(t):
	if len(t) > 2:
		return tuple(sorted(t)[1:-1])
	
# не міняйте наступний код
assert sort_and_strip(()) is None
assert sort_and_strip((1,)) is None
assert sort_and_strip((1, 2)) is None
assert sort_and_strip((1, 2, 3)) == (2,)
assert sort_and_strip((2, 1, 3, 1.5)) == (1.5, 2)