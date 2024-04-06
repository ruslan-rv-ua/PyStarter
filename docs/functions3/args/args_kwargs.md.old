---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

## Функції з довільною кількістю аргументів

Напишемо функцію, яка визначає суму трьох чисел:

	:::python
	>>> def adder(x, y, z):
	...     return x + y + z
	...
	>>> adder(10, 12, 13)
	35
	>>>	

Функція приймає 3 параметри. А що буде якщо передати функції більше трьох аргументів?

	:::python
	>>> adder(10, 12, 13, 15)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: adder() takes 3 positional arguments but 4 were given
	>>>
	
Цілком очікувано. 
Але було б непогано, якби існував механізм, щоб функції можна було передавати змінну кількість аргументів...

### `*args`

Використовуючи `*args` в параметрах функції ми цим самим вказуємо, що тут функція може отримати невизначену наперед кількість неіменованих аргументів.
Зірочка перед ідентифікатором означає, що це ім'я буде вказувати на кортеж, який і буде містити усі неіменовані аргументи, які ми передали функції.

Отже тепер наша функція може виглядати так:

	:::python
	def adder(*args):
		res = 0
		for num in args:
			res += num
		return res
	>>> adder(10, 12, 13, 15)
	50
	>>> adder(10, 12, 13, 15, 20, 70)
	140
	>>> adder(10)
	10
	>>> adder()
	0
	>>>	
		

### `**kwargs`

Для передачі довільної кількості іменованих аргументів використовуємо синтаксис `**kwargs`. У цьому випадку `kwargs` — словник, що містить імена аргументів та їх значення.

Створимо функцію, яка розповість про усі іменовані аргументи, що ми їй передали:

	:::python
	>>> def all_i_have_got(**kwargs):
	...     for key in kwargs:
	...             print(f'{key} is {kwargs[key]}')
	...
	>>> all_i_have_got(apple='red', size='big')
	apple is red
	size is big
	>>> all_i_have_got(item='Aplle iPhone 5s', price=99.99, colors=['black','silver'])
	item is Aplle iPhone 5s
	price is 99.99
	colors is ['black', 'silver']
	>>> all_i_have_got()
	>>> all_i_have_got(1)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: all_i_have_got() takes 0 positional arguments but 1 was given
	>>>

### Іменування

`args` і `kwargs` — це по суті звичайні параметри функції. 
Отже імена можна вказати будь-які, головне — це зірочки перед цими іменами. 
Однак за домовленістю прийнято називати такі параметри саме так: 

- `args` - скорочення від `ARGuments`
- `kwargs` — скорочення від `KeyWord ARGuments`
	
### Усі разом

Якщо є бажання використовувати `args` та `kwargs` разом, то робиться це наступним чином:

	def func(positional, *args, **kwargs)
	
Порядок слідування аргументів є важливим: спочатку позиційні аргументи, потім `args`, а вже за ними `kwargs`.

<!--
## Завдання

Напишіть функцію `my_min()`, яка повертає мінімальний з переданих їй аргументів. 
Кількість аргументів може бути довільною. 
Якщо функції не передано жодного аргументу, має виникати вийняткова ситуація. 
-->