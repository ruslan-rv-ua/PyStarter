'''
"Знайти котика"

Реалізуйте функцію find_cat().
Функція приймає символьний рядок string.
Повертає True якщо в string є усі символи з рядка "котик"
і розташовані у тому ж порядку як у рядку "котик".
В інших випадках повертає False.
Дивіться тести для кращого розуміння.
'''
def find_cat(string):
	# ваш код
	word = 'котик'
	expected_char = 0
	string_char = 0
	while expected_char < len(word) and string_char < len(string):
		if string[string_char] == word[expected_char]:
			expected_char += 1
		string_char += 1
	return expected_char == len(word)

assert find_cat('') == False
assert find_cat('котик') == True
assert find_cat('котик дуже гарний') == True
assert find_cat(' к о т и   к') == True
assert find_cat('котки') == False
assert find_cat('к1о1т1и1к') == True
assert find_cat('кожен кіт — аналітик') == True
