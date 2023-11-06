'''
"Старший удвічі"

Реалізуйте функцію twice_as_old().
Функція приймає два цілих числа:
1. вік батька, повних років
2. вік сина, повних років
Функція повертає скільки років тому батько був удвічі старшим за сина
або через скільки років батько буде удвічі старшим за сина.
Функції будуть передаватись тільки валідні дані.
'''
def twice_as_old(dad_years_old, son_years_old):
	# ваш код починається тут
	return abs(dad_years_old - 2 * son_years_old)
# не міняйте наступний код
assert twice_as_old(36,7) == 22
assert twice_as_old(55,30) == 5
assert twice_as_old(42,21) == 0
assert twice_as_old(22,1) == 20
assert twice_as_old(29,0) , 29
