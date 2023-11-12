orders = 0
profit = 0
f = open('sales_500000_records.csv', 'r', encoding='utf8')
headers = f.readline().strip().split(',')
country_index = headers.index('Country')
profit_index = headers.index('Total Profit')
for line in f:
	columns = line.strip().split(',')
	if columns[country_index] == 'Ukraine':
		orders += 1
		profit += float(columns[profit_index])
f.close()
print(f'Number of orders: {orders}')
print(f'Total profit: {profit}')
'''
"Продажі"

CSV (від англ. comma-separated values ‘значення, розділені комою’, 
— файловий формат, котрий є відмежовувальним форматом для представлення табличних даних, 
у якому поля відокремлюються символом коми та переходу на новий рядок. 
Як правило у першому рядку файла містяться назви стовпчиків таблиці.
Формат CSV використовується для перенесення даних між базами даних та програмами — редакторами електронних таблиць. 

У файлі "sales_500000_records.csv" містяться дані про замовлення в інтернет-магазині.
У стовпчику "Country" знаходиться назва країни, з якої було зроблено замовлення.
У стовпчику "Total Profit" знаходиться сумма замовлених товарів.

Порахуйте скільки і на яку суму було зроблено замовлень з України.

Приблизний результат:
Number of orders: 2758
Total profit: 1100572467.2799988
'''