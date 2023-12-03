'''
"Усі співають пісеньку!"

Реалізувати функцію create_song(), яка приймає 3 аргументи:
- repeats - кількість повторів складу "ла" через "-" які складають одне слово;
- words - кількість слів в кожому рядку;
- lines - кількість рядків у пісеньці.

Функція повинна повернути рядок з пісенькою.

Приклад:
create_song(3, 2, 2)
Повертає:
"""ла-ла-ла ла-ла-ла
ла-ла-ла ла-ла-ла"""
'''

# ваш код тут
def create_song(repeats, words, lines):
	word = '-'.join(['ла'] * repeats)
	line = ' '.join([word] * words)
	result = '\n'.join([line] * lines)
	return result

# юніт тест
assert create_song(3, 2, 2) == """ла-ла-ла ла-ла-ла\nла-ла-ла ла-ла-ла"""
assert create_song(5, 1, 3) == """ла-ла-ла-ла-ла\nла-ла-ла-ла-ла\nла-ла-ла-ла-ла"""
