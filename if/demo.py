total = 10
cash = 15

if cash >= total:
	# print('Дякуємо за покупку')
	# change = cash - total
	# print('Решта:', change)
print('До побачення')


print('До сплати:', total)
print('Готівка:', cash)
if cash >= total:
	print('Дякуємо за покупку')
	if cash != total:
		change = cash - total
		print('Решта:', change)
	else:
		print('Без решти')
else:
	print('Не вистачає коштів')
print('До побачення')

x = 10
if x < 0:
	result = -1
elif x > 0:
	result = 1
else:
	result = 0
print(result)

