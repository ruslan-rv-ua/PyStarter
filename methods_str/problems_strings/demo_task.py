'''
Поміняти місцями ім'я та прізвище.
'''

def name_shuffle(name):
	return ' '.join(name.split()[::-1])

assert name_shuffle('') == ''
assert name_shuffle('Bill') == 'Bill'
assert name_shuffle('Linus Torvalds') == 'Torvalds Linus'
assert name_shuffle('Jean-Michel Jarre') == 'Jarre Jean-Michel'
assert name_shuffle('Lara Croft') == 'Croft Lara'  
assert name_shuffle('   Harry     Potter    ') == 'Potter Harry'