'''
Написати функцію incrementer().
Приймає список натуральних чисел.
Функція має повернути новий список з обробленими числами зі вхідного списка.

Обробка вхідних чисел полягає у тому, що до кожного числа додається номер його позиції у спискові.
Позиції рахуємо з 1.
incrementer([1,2,3]) == [2,4,6]

Якщо ви отримуєте число з більше ніж одного знаків, тоді береться лише останній знак числа (остання його цифра).
incrementer([4,6,9,1,3]) == [5,8,2,5,8]
9 (число) + 3 (його позиція) == 12
Беремо лише останню цифру: 2
'''
# ваш код починається тут
def incrementer(array):
	res = []
	for pos, number in enumerate(array):
		res.append((array[pos] + pos + 1) % 10)
	return res

# не міняйте наступний код
assert incrementer([]) == []
assert incrementer([1,2,3]) == [2,4,6]
assert incrementer([4,6,7,1,3]) == [5,8,0,5,8]
assert incrementer([3,6,9,8,9]) == [4,8,2,2,4]
assert incrementer([1,2,3,4,5,6,7,8,9,9,9,9,9,8]) == [2,4,6,8,0,2,4,6,8,9,0,1,2,2]