'''
"Дайте поспати!"

Реалізуйте функцію sleep_in(weekday, vacation).
Параметр weekday визначає, чи зараз робочій день, можливі значення True або False.
Параметр vacation визначає. чи зараз ми у відпустці, можливі значення True або False.. 
Ми можемо поспати подовше у неробочі дні або коли у відпустці. 
Функція має повертати True, якщо ми можемо поспати подовше.
sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True
'''
def sleep_in(weekday, vacation):
	# ваш код починається тут
	return not weekday or vacation
# не міняйте наступний код
assert sleep_in(False, False) == True
assert sleep_in(True, False) == False
assert sleep_in(False, True) == True
assert sleep_in(True, True) == True