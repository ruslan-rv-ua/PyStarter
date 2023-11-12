'''
"Матриця"

Реалізуйте функцію print_matrix().
Функція отримує матрицю чисел — список, елементами якого є списки (рядки), елементами яких у свою чергу є цілі числа (колонки).
Функція виводить матрицю у вигляді таблиці.
Якщо функції передано матрицю
[[1,2,3],[4,5,6],[7,8,9]]
то вивід має бути наступним:
1 2 3
4 5 6
7 8 9
'''
def print_matrix(matrix):
	# ваш код тут
	row = 0
	while row < len(matrix):
		line = ''
		col = 0
		while col < len(matrix[row]):
			line += str(matrix[row][col]) + ' '
			col += 1
		print(line)
		row += 1
		
def print_matrix(matrix):
	print('\n'.join(('{:5} '*len(row)).strip().format(*row) for row in matrix))

matrix = [[1,2,3],[4,5,6],[7,8,9]]
# випадково сгенерована матриця, можна розкоментувати наступний код
'''
from random import randint
n = randint(3, 6)
matrix = [[randint(0, 9) for col in range(n)] for row in range(n)]
'''
print_matrix(matrix)