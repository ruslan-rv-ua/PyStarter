'''
"Прості числа"

Просте число - це число, яке ділиться націло тільки на 1 і на себе.
Напишіть функцію is_prime() яка отримує натуральне число.
Функція повертає True, якщо передане їй число є простим, і False в іншому випадку.
Використовуючи написану функцію виведіть у стовпчик перші 7 простих чисел починаючи з числа 2.
Очікуваний вивід:
2
3
5
7
11
13
17
'''
def is_prime(n):
	divider = 2
	while divider < n:
		if(n % divider == 0):
			return False
		divider += 1
	return True
	
number = 2
primes_count = 0
while primes_count < 7:
	if is_prime(number):
		print(number)
		primes_count += 1
	number += 1
