---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

# Модуль datetime

Модуль datetime з стандартної бібліотеки Python — це збірка з самих різних класів і методів для комфортної роботи з часом і датами. 
Дозволяє:

- отримувати поточні системні дату і час
- обчислювати різницю між датами та інші схожі операції
- порівнювати дати/час
- форматувати інформацю про дату/час

Далі розглядаються деякі класи і методи, 
а також основні прийоми роботи з датою і часом.

## Константи

В модулі містяться константи: 

- `MINYEAR = 1` — мінімальне значення року
- `MAXYEAR = 9999` — максимальне значення року

## Класи

- `timedelta` — описує певний період часу між двома різними моментами
- `tzinfo` — дані про часовий пояс, абстрактний клас
- `timezone` — дані про часовий пояс у форматі UTC
- `time` — дані про час
- `date` — дані про дату на основі Григоріанського календаря
- `datetime` — дані про дату і час

### date

	datetime.date(year, month, day)
	
- datetime.MINYEAR ≤ year ≤ datetime.MAXYEAR
- 1 ≤ month ≤ 12
- 1 ≤ day ≤ кількість днів у відповідному місяці і році

Клас використовується для представлення даних про дату, які включають рік, місяць та число.

	>>> from datetime import date
	>>> a = date(2019, 10, 1)
	>>> a
	datetime.date(2019, 10, 1)
	>>> print(a)
	2019-10-01
	>>>

Об'єкти немутабельні:

	>>> a.year
	2019
	>>> a.month
	10
	>>> a.day = 2
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	AttributeError: attribute 'day' of 'datetime.date' objects is not writable
	>>>

Отримати поточну дату можна за допомогою метода today():

	>>> date.today()
	datetime.date(2019, 10, 1)
	>>>

### time

	datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None)
	
- 0 ≤ hour < 24
- 0 ≤ minute < 60
- 0 ≤ second < 60
- 0 ≤ microsecond < 1000000

Клас використовується для представлення даних про час, 
які включають години, хвилини, секунди та мікросекунди.

	>>> from datetime import time
	>>> a=time(15, 3, 0)
	>>> a
	datetime.time(15, 3)
	>>> print(a)
	15:03:00
	>>> a.hour
	15
	>>> a.second
	0
	>>> a.second = 1 # immutable!
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	AttributeError: attribute 'second' of 'datetime.time' objects is not writable
	>>>
	
### datetime

	datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None
	
Клас є комбінацією дати і часу.

	>>> from datetime import datetime
	>>> a=datetime(2019, 10, 1)
	>>> a
	datetime.datetime(2019, 10, 1, 0, 0)
	>>> print(a)
	2019-10-01 00:00:00
	>>> a=datetime(2019, 10, 1, 15, 59)
	>>> a
	datetime.datetime(2019, 10, 1, 15, 59)
	>>> print(a)
	2019-10-01 15:59:00
	>>>
	
Поточні дата і час — метод now():

	>>> a = datetime.now()
	>>> a
	datetime.datetime(2019, 10, 1, 15, 14, 22, 319901)
	>>> print(a)
	2019-10-01 15:14:22.319901
	>>>

Атрибути такі ж як у попередніх класів:

	>>> a.day
	1
	>>> a.year
	2019
	>>> a.hour
	15
	>>> a.second
	22
	>>>
	
"Відокремити" дату і час:


	>>> a.date()
	datetime.date(2019, 10, 1)
	>>> a.time()
	datetime.time(15, 14, 22, 319901)
	>>>

#### Форматування дат і часу

Класи datetime, date, time містять метод strftime. 
Цей метод дозволяє створювати символьний рядок, який відображає час у більш зрозумілій для людини формі.

	strftime(format)
	
`format` — символьний рядок, містить параметри форматування. 
Існує багато параметрів форматування, ознайомитись з усіма можна у відповідній документації. 
Далі розглянуто лише деякі.

	>>> from datetime import datetime as dt
	>>> a = dt.now()
	>>> a
	datetime.datetime(2019, 10, 3, 17, 42, 46, 921876)
	>>> a.strftime('%Y/%m/%d')
	'2019/10/03'
	>>> a.strftime('%Y, %B %d')
	'2019, October 03'
	>>> a.strftime('%d %h %Y')
	'03 Oct 2019'
	>>> a.strftime('%H:%M:%S')
	'17:42:46'
	>>> a.strftime('%H:%M')
	'17:42'
	>>>
	
#### Парсинг дат і часу

Якщо маємо символьний рядок який містить дату/час а необхідно отримати відповідний об'єкт, використовуємо `strptime()`:

	strptime(date_string, format)
	
Метод перетворює символьний рядок на об'єкт дати/часу:

	>>> s='2019===10-3'
	>>> datetime.datetime.strptime(s, '%Y===%m-%d')
	datetime.datetime(2019, 10, 3, 0, 0)
	>>>
	
### timedelta

	datetime.timedelta(days=0, seconds=0, microseconds=0)
	
Різниця між двома моментами часу, з точністю до мікросекунд.

	>>> from datetime import timedelta
	>>> birthdate = datetime(1970,1,1)
	>>> uptime = datetime.now() - birthdate
	>>> uptime
	datetime.timedelta(18170, 70930, 703964)
	>>> print(uptime)
	18170 days, 19:42:10.703964
	>>> uptime.days
	18170
	>>> uptime.seconds
	70930
	>>>
## Додаткові матеріали

- [Документація: модуль datetime](https://docs.python.org/3/library/datetime.html)
- [Arrow: Better dates & times for Python](https://pypi.org/project/arrow/)
- [Pendulum: Python datetimes made easy.](https://pypi.org/project/pendulum/)
- [dateutil - powerful extensions to datetime](https://pypi.org/project/python-dateutil/)
- [Delorean: Time Travel Made Easy](https://pypi.org/project/Delorean/)
