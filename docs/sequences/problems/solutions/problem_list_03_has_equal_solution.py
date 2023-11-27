'''
"Щось у них є спільне"

Реалізуйте функцію has_equal():
1. В параметрах отримує два списки
2. Якщо в двох списках є хоча б один однаковий елемент, тобто такі елементи, що мають однакове значення,
то функція повертає True
3. Інакше повертає False
'''
def has_equal(list1, list2):
	# ваш код тут
	index = 0
	while index < len(list1):
		if list1[index] in list2:
			return True
		index += 1
	return False

# тести, не чіпати!
assert has_equal([], []) == False
assert has_equal([], [1]) == False
assert has_equal([1], []) == False
assert has_equal([1], [1]) == True
assert has_equal([[1]], [1]) == False
assert has_equal([1], [3, 2, 1]) == True
assert has_equal([1, 2, 3], [5, 4, 3]) == True
assert has_equal([1, 2, 3], [1]) == True
