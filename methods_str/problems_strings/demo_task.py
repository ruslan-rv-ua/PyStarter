'''
Поміняти місцями ім'я та прізвище.
'''

def name_shuffle(name):
	return ' '.join(name.split()[::-1])

assert name_shuffle("Donald Trump") == "Trump Donald"
assert name_shuffle("Rosie O'Donnell") == "O'Donnell Rosie"
assert name_shuffle("Seymour Butts") == "Butts Seymour"