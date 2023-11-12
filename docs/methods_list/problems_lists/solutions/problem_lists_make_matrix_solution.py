'''
"Створити матрицю"

Реалізуйте функцію make_matrix(n, value)
Елементами матриці можуть бути не лише числа, а будь-які об'єкти.
Функція створює і повертає матрицю розміром n на n заповнену значенням value.
'''
def make_matrix(n, value):
	# починайте кодити тут
	matrix = []
	for r in range(n):
		row = []
		for c in range(n):
			row.append(value)
		matrix.append(row)
	return matrix
	
# тести, не міняйте наступний код
from functools import reduce
m = make_matrix(3, 5)
assert sum(reduce(list.__add__, m)) == 45
m[0][0] = 11
assert sum(reduce(list.__add__, m)) == 51
m[-1][-1] = 11
assert sum(reduce(list.__add__, m)) == 57