MONTH_NAMES = tuple(
'Січень Лютий Березень Квітень Травень Червень Липень Серпень Вересень Жовтень Листопад Грудень'.split()
)

rates = {}
in_file = open('market-price.csv', 'r', encoding='utf8')
for line in in_file:
	data = line.strip().split(',')
	date = data[0].split('-')
	if date[0] != '2017':
		continue
	price = float(data[1])
	month = int(date[1])
	if month in rates:
		rates[month].append(price)
	else:
		rates[month] = [price]
in_file.close()

out_file = open('report.csv', 'w', encoding='utf8')
for month in sorted(rates):
	avg_price = int(sum(rates[month]) / len(rates[month]))
	line = f'{MONTH_NAMES[month-1]},{avg_price}'
	print(line, file=out_file)
out_file.close()
'''
"Знав би прикуп"

У файлі market-price.csv записано курс Bitcoin у доларах США.
У кожному окремому рядку міститься курс за певну дату.
Дата і курс у рядку розділено знаком коми.
Дата має наступний формат:
- рік (4 цифри)
- знак дефісу
- місяць (2 цифри)
- знак дефісу
- число місяця (2 цифри)

Файл у кодуванні UTF-8.

Напишіть програму яка визначає середній курс Bitcoin за кожен місяць.
Курс округлити до цілого.
Враховувати дані тільки за 2017 рік.
Результати записати у текстовий файл "avg_btc.csv" у такому форматі:
<місяць прописом>,<курс>
наприклад:
січень,5083
'''
