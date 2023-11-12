﻿'''
"Банкомат"

ПІН-код банківської картки користувача: 1111
Напишіть програму яка:
1. Просить користувача ввести ПІН-код до картки.
2. Якщо користувач ввів невалідний ПІН-код (щось інше ніж чотири цифри), програма повідомляя користувача про це і переходимо до пункту 1.
3. Якщо користувач ввів правильний ПІН-код, програма виводить "Доступ дозволено" і завершує роботу.
4. Інакше переходимо до пункту 1, але користувач має лише три спроби ввести валідний ПІН.
5. Якщо після трьох спроб користувач не ввів правильний код, програма виводить "Доступ заборонено" і завершує роботу.
'''
PIN = '1111'
# ваш код починається тут
for _ in range(3):
	while True:
		answer = input('Введіть ПІН: ')
		if len(answer) == 4 and answer.isdigit():
			break
	if answer == PIN:
		print('Ласкаво просимо')
		break
	print('Невірний ПІН')
else:
	print('Доступ заборонено')
