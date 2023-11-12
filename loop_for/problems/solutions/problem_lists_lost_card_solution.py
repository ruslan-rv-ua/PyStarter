'''
"Пропала картка"

Для настольлної гри використовують картки з номерами від 1 до N.
Одну картку згубили.
Реалізуйте функцію find_lost_card(cards).
Функція приймає список з номерами карток.
Функція повертає номер відсутньої картки.
Перевірка.
Вхідні дані: [1, 2, 3, 4]
Результат: 5
Вхідні дані: [2, 3, 4, 5]
Результат: 1
'''
def find_lost_card(cards):
	return sum(range(len(cards) + 2)) - sum(cards)
	
def find_lost_card(cards):
	for card in range(1, len(cards) + 2):
		if card not in cards:
			return card
	
assert find_lost_card([1, 2, 3, 4]) == 5
assert find_lost_card([2, 3, 4, 5]) == 1
assert find_lost_card([1, 3, 4, 5]) == 2
assert find_lost_card([4, 1, 7, 8, 3, 5, 9, 10, 6]) == 2