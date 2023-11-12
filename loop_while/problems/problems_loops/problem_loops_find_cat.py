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

assert find_cat('') == False
assert find_cat('котик') == True
assert find_cat('котик дуже гарний') == True
assert find_cat(' к о т и   к') == True
assert find_cat('котки') == False
assert find_cat('к1о1т1и1к') == True
assert find_cat('кожен кіт — аналітик') == True
