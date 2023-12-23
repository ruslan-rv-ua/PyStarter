---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

## Лише позиційні або іменовані

<!-- https://www.python.org/dev/peps/pep-0570/#how-to-teach-this -->

В Python є можливість явно вказати, щоб частина аргументів завжди передавалась тільки як позиційні або тільки як ключові. 
Узагальнено визначення функції виглядає так: 

	:::python
	def f(pos1, pos2, /, pos_or_kwd1, pos_or_kwd2, *, kwd1, kwd2):
	
Аргументи можуть передаватись:

- pos1, pos2 — лише як позиційні
- pos_or_kwd1, pos_or_kwd2 — як позиційні або ключові
- kwd1, kwd2 — лише як ключові

### Приклади

Функції `standard_arg` можна передавати як позиційні, так і іменовані аргументи:

	:::python
	>>> def standard_arg(arg):
	...     print(arg)
	>>> standard_arg(2)
	2
	>>> standard_arg(arg=2)
	2

Функції `pos_only_arg` можна передавати лише позиційні аргументи:

	:::python
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
	
	:::python
	>>> def kwd_only_arg(*, arg):
	...     print(arg)
	>>> kwd_only_arg(3)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: kwd_only_arg() takes 0 positional arguments but 1 was given
	>>> kwd_only_arg(arg=3)
	3
	
І нарешті функція яка використовує усе одразу:
	
	:::python
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

	:::python
	def sin(x, /): 
	
Функції ми передаємо лише одне число, і це просто число. Заплутатись важко, ім'я вказувати недоречно. 

А ось ще одна функція з модуля `json`:

	:::python
	def dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)
	
Передаємо функції лише один якийсь об'єкт, а потім можна вказати ще багато аргументів. 
Запам'ятати порядок цих аргументів практично неможливо, тому легко заплутатись що саме ми передаємо коли викликаємо функцію. 
Оголосивши параметри як лише іменовані ми не зможемо передати аргумент без імені, 
тому помилитись неможливо:

	:::python
	dumps(some_object, indent=2, sort_keys=False)

