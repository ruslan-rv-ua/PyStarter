'''
"Послідовність Фібоначчі"

Реалізуйте функцію make_fibo_sequence(n).
Отримує натуральне число n > 1.
Повертає послідовність числе Фібоначчі довжиною n у вигляді списка.
'''
def make_fibo_sequence(n):
	# ваш код тут
	fibo = [1, 1]
	for _ in range(n - 2):
		fibo.append(fibo[-2] + fibo[-1])
	return fibo

# тести
assert make_fibo_sequence(2) == [1, 1]
assert make_fibo_sequence(3) == [1, 1, 2]
assert make_fibo_sequence(5) == [1, 1, 2, 3, 5]
assert make_fibo_sequence(10) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]