'''
"Усе спільне"

Реалізуйте функцію intersection():
В параметрах отримує два списки
Повертає список який містить спільні (рівні по значенню) елементи для двох списків.
'''
def intersection(list1, list2):
	# ваш код тут

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


