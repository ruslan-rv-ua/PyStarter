'''
"Максимум з 3"

Напишіть програму яка виконує наступне:
1. Просить користувача послідовно ввести три цілих числа
2. Виводить найбільше з цих чисел
'''
# ваш код починається тут
n1 = int(input('Enter integer 1'))
n2 = int(input('Enter integer 2'))
n3 = int(input('Enter integer 3'))
'''
if n1 > n2:
	max = n1
else:
	max = n2
if n3 > max:
	max = n3
'''
max = n1 if n1 > n2 else n2
max = n3 if n3 > max else max
print(max)
