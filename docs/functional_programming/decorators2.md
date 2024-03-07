---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

Давайте на прикладах розглянемо як можна використовувати декоратори.

### Визначити хто швидше
	
Напишемо функцію яка повертає символьний рядок з одного мільйона пробілів.
Задачу можна вирішити декількома способами, наприклад:

```python
def f1():
	res = ' ' * 10**6

def f2():
	res = ''
	for i in range(10**6):
		res += ' '
```	

А яка з функцій буде виконуватись швидше? 
Щоб з'ясувати, давайте просто заміряємо час який треба на виконання кожної з функцій.

Для вимірювання часу скористаємось функцією `perf_counter()` з модуля `time`:

```python
from time import perf_counter

def f1():
	t = perf_counter()
	res = ' ' * 10**6
	print(f"f1: {perf_counter()-t}")
```	

Ми написали код для функції `f1()`, який вимірює і виводить час необхідний для виконання цієї функції. 
І вже тут ми бачимо наступні недоліки:

* ми змінили функцію, час роботи якої хочемо вимірювати
* для інших функції для вирішення задачі так само треба буде змінити код, причому код цей буде кожного разу повторюватись

А чи не можна було б зробити таку штуку, щоб кожна функція вимірювала і виводила б час потрібний на її виконання? І тут на допомогу приходять декоратори. За допомогою декоратора ми зможемо як би розширити можливості функції, що передамо йому.

```python
from time import perf_counter

def timeit(func):
	def wrapper():
		t = perf_counter()
		func()
		print(f"{func.__name__}: {perf_counter()-t}")
	return wrapper
```

Тепер просто декоруємо наші функції:

```python
@timeit
def f1():
	res = ' ' * 10**6

@timeit
def f2():
	res = ''
	for i in range(10**6):
		res += ' '
```

І, власне, визначаємо хто швидше:

	>>> f1()
	f1: 0.0005259999888949096
	>>> f2()
	f2: 0.17047839998849668
	>>>



### Ланцюжки з декораторів

Синтаксис Python дозволяє одночасне використання декількох декораторів.

	:::python
	>>> def bread(func):
	...     def wrapper():
	...             print('Хліб')
	...             func()
	...             print('Хліб')
	...     return wrapper
	...
	>>> def salad(func):
	...     def wrapper():
	...             print('Зеленина')
	...             func()
	...             print('Зеленина')
	...     return wrapper
	...
	>>> @bread
	... @salad
	... def stake():
	...     print("М'ясо")
	...
	...
	>>> stake()
	Хліб
	Зеленина
	М'ясо
	Зеленина
	Хліб
	>>>
	
Застосування тих самих декораторів, але без "магічного" символа `@`:

	:::python
	stake = bread(salad(stake))

Зауважте що послідовність застосування декораторів має значення:

	:::python
	>>> @salad
	... @bread
	... def stake():
	...     print("М'ясо")
	...
	>>> stake()
	Зеленина
	Хліб
	М'ясо
	Хліб
	Зеленина
	>>>

		
		
		
		
		
### Декоруємо функції з параметрами

У попередніх прикладах ми декорували функції, які не мали ніяких параметрів. А як щодо функцій з параметрами?

Припустимо маємо таку функцію:

	:::python
	>>> def div(a, b):
	...     return a / b
	...
	>>>
	
При певних умовах ми отримаємо помилку:
	
	:::python
	>>> div(2, 0)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	  File "<stdin>", line 2, in div
	ZeroDivisionError: division by zero
	>>>

Давайте спробуємо створити декоратор, який буде перевіряти вхідні параметри функції:

	:::python
	>>> def smart_div(func):
	...     def wrapper(a, b):
	...             print("I am going to divide",a,"and",b)
	...             if b == 0:
	...                     print("Oops! cannot divide")
	...                     return
	...             return func(a, b)
	...     return wrapper
	...
	>>>

Такий варіант поверне `None` якщо умова спрацює:

	:::python
	>>> @smart_div
	... def div(a, b):
	...     return a / b
	...
	>>> div(1, 0)
	I am going to divide 1 and 0
	Oops! cannot divide
	>>> div(1, 1)
	I am going to divide 1 and 1
	1.0
	>>>

Можна зауважити, параметри вкладеної функції-обгортки `wrapper()` всередині декоратора такі самі як і у функції, що декорується. Знаючи це ми можемо створити "загальний" декоратор, який буде працювати з будь-якою кількістю параметрів.

Напишемо декоратор, який буде повідомляти нам, що ми передали функції, яку він декорує:

	:::python
	>>> def works_for_all(func):
	...     def wrapper(*args, **kwargs):
	...             print('I got next parameters:', args, kwargs)
	...             return func(*args, **kwargs)
	...     return wrapper
	...
	>>> @works_for_all
	... def f(a, b):
	...     pass
	...
	>>> f('string', b=123)
	I got next parameters: ('string',) {'b': 123}
	>>>
	

### Декоратори з параметрами

Давайте напишемо декоратор, який буде готувати нам сендвічі:

	:::python
	>>> def make_sandwich(func):
	...     def wrapper(sandwich_with):
	...             print('Хліб')
	...             func(sandwich_with)
	...             print('Хліб')
	...     return wrapper
	...
	>>> @make_sandwich
	... def sandwich(sandwich_with):
	...     print(sandwich_with)
	...
	>>> sandwich("М'ясо")
	Хліб
	М'ясо
	Хліб
	>>>

Непогано. Але як щодо ситуації, коли для приготування сендвіча ми захочемо використовувати не хліб, а, припустимо, тости? Напрошується ідея повідомити декоратору що ми хочемо використовувати в якості "обгортки" нашого сендвіча, тобто передати декоратору якісь параметри.

Отже, декоратор приймає свої параметри, але потім він ще має прийняти функцію, яку має декорувати, а потім ще й аргументи декорованої функції. Таким чином нам доведеться зробити аж 3 функції:

	:::python
	>>> def make_sandwich(sandwich_cover):
	...     def decorator(func):
	...             def wrapper(sandwich_with):
	...                     print(sandwich_cover)
	...                     func(sandwich_with)
	...                     print(sandwich_cover)
	...             return wrapper
	...     return decorator
	...
	>>> @make_sandwich('Тост')
	... def sandwich(sandwich_with):
	...     print(sandwich_with)
	...
	>>> sandwich("Ковбаса")
	Тост
	Ковбаса
	Тост
	>>> @make_sandwich('Хліб')
	... def sandwich(sandwich_with):
	...     print(sandwich_with)
	...
	>>> sandwich("Сало")
	Хліб
	Сало
	Хліб
	>>>

Функція `make_sandwich` приймає в якості параметра "обгортку" для сендвіча `sandwich_cover` і повертає функцію `decorator` яка, як і раніше, приймає тільки функцію що треба декорувати і повертає свою внутрішню функцію `wrapper`, яка у свою чергу приймає аргументи декорованої функції `func`.

Те ж саме можна написати "без магії":

	:::python
	>>> def sandwich(sandwich_with):
	...     print(sandwich_with)
	...
	>>> sandwich = make_sandwich('Хліб')(sandwich)
	>>> sandwich("Сало")
	Хліб
	Сало
	Хліб
	>>>

З декораторів з параметрами теж можна будувати ланцюжки:

	:::python
	>>> @make_sandwich('Хліб')
	... @make_sandwich('Хрін')
	... def super_sandwich(sandwich_with):
	...     print(sandwich_with)
	...
	>>> super_sandwich("Сало")
	Хліб
	Хрін
	Сало
	Хрін
	Хліб
	>>>
	
### Клас-декоратор
<!-- https://habr.com/ru/post/587066/ -->

Отже щоб створити декоратор з параметрами ми використовували три вкладені одна в одну функції. 
Виглядає трішечки монструозно...
І саме так було прийнято писати параметризовані декоратори, 
доки комусь у голову не прийшла світла думка, 
що декоратор можна створити у вигляді класа. 

По суті нам необхідно розділити етапи створення з запам'ятовуванням 
переданих параметрів і виклика, 
тобто зробити те, що роблять класи. 

	:::python
	class sandwich_cover:
		def __init__(self, cover):
			self._cover = cover
			
		def __call__(self, func):
			def wrapper(sandwich_with):
				print(self._cover)
				func(sandwich_with)
				print(self._cover)
			return wrapper

Приготуємо "класний" сендвіч:
		
	:::python
	>>> @sandwich_cover('Тост')
	... @sandwich_cover('Хрін')
	... def sandwich(sandwich_with):
	...     print(sandwich_with)
	...
	>>> sandwich("Ковбаса")
	Тост
	Хрін
	Ковбаса
	Хрін
	Тост
	>>>

Код виглядає набагато читабельнішим. 
Залишилось лише змиритись з назвою класа з маленької букви, 
або ж з назвою декоратора з великої 😊.

### Декорування класів

Декорувати можна не лише функції, але і класи. 
Реалізуємо декоратор, 
який додає до класа метод для представлення класа у вигляді символьного рядка: 

	:::python
	def auto_str_class(any_class):
		def str(self):
			variables = (f'{key}={value!r}' for key, value in vars(self).items())
			return f'{any_class.__name__}({", ".join(variables)})'
		
		any_class.__str__ = str
		return any_class

Тепер декоровані класи можуть детальнло розказати про себе:

	:::python
	>>> @auto_str_class
	... class Person:
	...     def __init__(self, name, age):
	...         self.name = name
	...         self.age = age
	...
	>>> p = Person('Jane', 26)
	>>> print(p)
	Person(name='Jane', age=26)
	>>>


## Резюме

* декоратор — спосіб модифікувати поведінку функції, зберігаючи читабельність кода
* декоратори дещо сповільнюють виклики функцій
* порядок вказання декораторів має значення	
* клас може виступати декоратором
* декорувати можна не лише функції, але і класи
