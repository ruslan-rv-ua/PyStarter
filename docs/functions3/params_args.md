---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

# Параметри і аргументи функцій

Викликаючи функцію, ми можемо передавати їй наступні типи аргументів:

* позиційні аргументи (positional arguments)
* іменовані аргументи (keyword arguments)
* опційні аргументи (default arguments)
* аргумети довільної довжини (variable-length argumens)


## Позиційні аргументи

Коли викликаємо функцію фактичні параметри заміщують формальні у тому порядку, у якому їх вказано.

	>>> def product_info(name, color, price):
	...     print('Product:', name)
	...     print('Color:', color)
	...     print('Price:', price)
	...
	>>> product_info('Pen', 'blue', 2)
	Product: Pen
	Color: blue
	Price: 2
	>>>
	>>> product_info(2, 'Pen', 'blue')
	Product: 2
	Color: Pen
	Price: blue
	>>>

## Іменовані аргументи

Ми маємо можливість змінити порядок слідування аргументів. Для цього при вказанні значень аргументів необхідно вказувати також ї імена відповідних параметрів функції у вигляді:

`параметр=значення`

Подивимось як можна викликати попередньо написану функцію:

	>>> product_info(price=2, name='Pen', color='blue')
	Product: Pen
	Color: blue
	Price: 2
	>>>

При викликах функцій можна одночасно використовувати як позиційні, так і іменовані аргументи. Спочатку треба вказати певну кількість позиційних аргументів, які будуть заміщати відповідні їм по порядку параметри, а потім для усіх аргументів, що залишились, вказуємо іменовані аргументи у довільному порядку:

	>>> product_info('Pen', price=2, color='blue')
	Product: Pen
	Color: blue
	Price: 2
	>>>

У прикладі вище перший аргумент буде відповідати параметру функції `name`, інші ж аргументи ми вказали з іменами параметрів.

Спроба вказати позиційний аргумент після іменованих призведе до відповідної помилки:

	>>> product_info(price=2, color='blue', 'Pen')
	  File "<stdin>", line 1
	SyntaxError: positional argument follows keyword argument
	>>>

## Опційні аргументи

Деякі параметри функції можна зробити необов'язковими. 
Для цього для них при визначенні функції треба вказати значення за замовчуванням. 
Це значення буде присвоєно параметру якщо ми викликаючи функцію не вкажемо відповідний аргумент:

	>>> def product_info(name, color='blue', price=7):
	...     print('Product:', name)
	...     print('Color:', color)
	...     print('Price:', price)
	...
	>>> product_info('Pen')
	Product: Pen
	Color: blue
	Price: 7
	>>> product_info('Pen', 'red')
	Product: Pen
	Color: red
	Price: 7
	>>> product_info('Pen', price=5)
	Product: Pen
	Color: blue
	Price: 5
	>>>

Такі аргументи називають опційними або ж аргументами за замовчуванням (default arguments). 
	
### Створення значень опційних параметрів
	
!!! warning "***Зауважте:***"
    значення за замовчуванням обчислюються і створюються лише один раз, 
    а саме при створенні функції! 
    У цей момент вони зв'язуються з іменами відповідних параметрів. 

Тому будьте обережними якщо у якості значення за замовчуванням вказуєте мутабельні об'єкти. 

	>>> def modify_list(lst=[]):
	...     lst.append(1)
	...     return lst
	...
	>>> l = modify_list()
	>>> l
	[1]
	>>> l = modify_list()
	>>> l
	[1, 1]
	>>>
	
Намагайтесь не використовувати мутабельні типи у якості значень за замовчуванням, 
якщо, звісно, ви чітко не усвідомлюєтє що саме робите. 
Вищенаведений код краще написати так:

	>>> def modify_list(lst=None):
	...     if lst is None:
	...             lst = []
	...     lst.append(1)
	...     return lst
	...
	>>> l = modify_list()
	>>> l
	[1]
	>>> l = modify_list()
	>>> l
	[1]
	>>>
	
## Лише позиційні або іменовані

<!-- https://www.python.org/dev/peps/pep-0570/#how-to-teach-this -->

В Python є можливість явно вказати, щоб частина аргументів завжди передавалась тільки як позиційні або тільки як ключові. 
Узагальнено визначення функції виглядає так: 

	def f(pos1, pos2, /, pos_or_kwd1, pos_or_kwd2, *, kwd1, kwd2):
	
Аргументи можуть передаватись:

- pos1, pos2 — лише як позиційні
- pos_or_kwd1, pos_or_kwd2 — як позиційні або ключові
- kwd1, kwd2 — лише як ключові

### Приклади

Функції `standard_arg` можна передавати як позиційні, так і іменовані аргументи:

	>>> def standard_arg(arg):
	...     print(arg)
	>>> standard_arg(2)
	2
	>>> standard_arg(arg=2)
	2

Функції `pos_only_arg` можна передавати лише позиційні аргументи:

	>>> def pos_only_arg(arg, /):
	...     print(arg)
	>>> pos_only_arg(1)
	1
	>>> pos_only_arg(arg=1)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: pos_only_arg() got an unexpected keyword argument 'arg'
	>>>
	
Функції `kwd_only_arg` можна передавати лише позиційні аргументи:
	
	>>> def kwd_only_arg(*, arg):
	...     print(arg)
	>>> kwd_only_arg(3)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: kwd_only_arg() takes 0 positional arguments but 1 was given
	>>> kwd_only_arg(arg=3)
	3
	
І нарешті функція яка використовує усе одразу:
	
	>>> def combined_example(pos_only, /, standard, *, kwd_only):
	...     print(pos_only, standard, kwd_only)
	>>> combined_example(1, 2, 3)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: combined_example() takes 2 positional arguments but 3 were given
	>>> combined_example(1, 2, kwd_only=3)
	1 2 3
	>>> combined_example(1, standard=2, kwd_only=3)
	1 2 3
	>>> combined_example(pos_only=1, standard=2, kwd_only=3)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: combined_example() got an unexpected keyword argument 'pos_only'

- використовуйте тільки позиційні якщо імена не мають значення або не несуть смислового навантаження, 
також кількість передаваних аргументів невелика і передаються вони завжди у тому ж самому порядку
- використовуйте тільки іменовані якщо імена мають смислове значення значення і у функції багато параметрів

Подивимось визначення функції `sin()` з модуля `math`:

	def sin(x, /): 
	
Функції ми передаємо лише одне число, і це просто число. Заплутатись важко, ім'я вказувати недоречно. 

А ось ще одна функція з модуля `json`:

	def dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)
	
Передаємо функції лише один якийсь об'єкт, а потім можна вказати ще багато аргументів. 
Запам'ятати порядок цих аргументів практично неможливо, тому легко заплутатись що саме ми передаємо коли викликаємо функцію. 
Оголосивши параметри як лише іменовані ми не зможемо передати аргумент без імені, 
тому помилитись неможливо:

	:::python
	dumps(some_object, indent=2, sort_keys=False)




## Функції з довільною кількістю аргументів

Напишемо функцію, яка визначає суму трьох чисел:

	>>> def adder(x, y, z):
	...     return x + y + z
	...
	>>> adder(10, 12, 13)
	35
	>>>	

Функція приймає 3 параметри. А що буде якщо передати функції більше трьох аргументів?

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