'''
"Матриця"
Завдання підвищеної складності.

Реалізуйте функцію make_matrix(n, value).
n — ціле число.
value — будь-яке значення.
Якщо n > 0, функція повертає матрицю розміром n на n заповнену значенням value.
Інакше функція повертає None.
Реалізуйте функцію print_matrix(matrix).
Функція виводить матрицю по рядкам. Приклад.
m = make_matrix(4, 7)
print_matrix(m)
Вивід:
7 7 7 7
7 7 7 7
7 7 7 7
7 7 7 7
>>>
Спробуйте створити і вивести матриці різних розмірностей з різними значеннями.
Тести до функції make_matrix() можуть стати у нагоді.
'''
def make_matrix(n, value):
	# ваш код тут
	if n > 0:
		matrix = [[value] * n][::] * n
		return matrix

	
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

		
m = make_matrix(3, 1)
m[0][0] = 7
# тести, не чіпати!
assert make_matrix(0, 7) == None
assert make_matrix(1, True) == [[True]]
assert make_matrix(2, 7) == [[7, 7], [7, 7]]
assert make_matrix(3, 'x') == [['x', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']]
assert make_matrix(4, None) == [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]