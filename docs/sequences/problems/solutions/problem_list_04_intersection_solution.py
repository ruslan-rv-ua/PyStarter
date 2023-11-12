'''
"Усе спільне"

Реалізуйте функцію intersection():
В параметрах отримує два списки
Повертає список який містить спільні (рівні по значенню) елементи для двох списків.
'''
def intersection(list1, list2):
	# ваш код тут
	res = []
	index = 0
	while index < len(list1):
		if list1[index] in list2:
			res += [list1[index]]
		index += 1
	return res

# тести, не чіпати!
fixtures = (
	([], [], []),
	([], [1], []),
	([1], [], []),
	([1], [1], [1]),
	([1], [1, 2], [1]),
	([1, 2], [1], [1]),
	([1, 2], [1, 2], [1, 2]),
	([2, 1], [1, 2], [1, 2]),
)
for f in fixtures:
	assert set(intersection(f[0], f[1])) == set(f[2])


