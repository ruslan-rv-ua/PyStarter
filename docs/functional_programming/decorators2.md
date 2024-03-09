---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

Розглянемо на прикладах як і для чого використовують декоратори.

### "Всім по одному"

А давайте напишемо декоратор, який дозволить викликати функції лише один раз.

```python
def run_once(func):
    called = False
    def wrapper(*args, **kwargs):
        nonlocal called
        if not called:
            called = True
            return func(*args, **kwargs)
        raise RuntimeError("Вже викликали цю функцію")
    return wrapper
	
@run_once
def f():
	print('функція запущена')
```

Тепер можна викликати функцію лише один раз:

	>>> f()
	функція запущена
	>>> f()
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	File "e:\dev\PyStarter\docs\functional_programming\demo3_decorator\e22_run_once.py", line 8, in wrapper
		raise RuntimeError("Вже викликали цю функцію")
	RuntimeError: Вже викликали цю функцію
	>>>

А як щодо функції `print()`? 
Оскыльки ця функція вже десь визначена, декоруємо її "вручну":

	>>> print = run_once(print)
	>>> print('Hey!')
	Hey!
	>>> print('Hey!')
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	File "e:\dev\PyStarter\docs\functional_programming\demo3_decorator\e22_run_once.py", line 8, in wrapper
		raise RuntimeError("Вже викликали цю функцію")
	RuntimeError: Вже викликали цю функцію
	>>>

Пам'ятаючи, що функція — це об'єкт, функціям можна задавати атрибути. 
Скористаємось цим і створимо декоратор трохи інакше:

```python
def run_once(func):
    def wrapper(*args, **kwargs):
        if not wrapper.called:
            wrapper.called = True
            return func(*args, **kwargs)
        raise RuntimeError("Вже викликали цю функцію")
    wrapper.called = False
    return wrapper
	
@run_once
def f():
	print('функція запущена')
```

Тепер можна визначити, чи було вже викликано цю функцію:

	>>> f.called
	False
	>>> f()
	функція запущена
	>>> f.called
	True
	>>> f()
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	File "e:\dev\PyStarter\docs\functional_programming\demo3_decorator\e22_run_once.py", line 29, in wrapper
		raise RuntimeError("Вже викликали цю функцію")
	RuntimeError: Вже викликали цю функцію
	>>>

### "Хто швидше?"
	
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






### Мемоізація

> ***Мемоізація*** — техніка кешування результатів функції для певних вхідних параметрів, щоб уникнути повторного обчислення результату при наступних викликах функції з тими ж параметрами. 

Створимо декоратор для кешування результатів функції:

```python
def memoize(func):
	cache = {}
	def wrapper(*args, **kwargs):
		key = (args, tuple(kwargs.items()))  # унікальний ключ для кешу
		if key not in cache:
			cache[key] = func(*args, **kwargs)
		return cache[key]
	return wrapper
```

* Декоратор `memoize` використовує словник `cache` для зберігання результатів попередніх викликів функції.
* Створюється унікальний ключ для кожного набору аргументів (`args` та `kwargs`). Цей ключ використовується для пошуку відповідного результату в кеші.
* Якщо ключ не знайдено в кеші, функція `func` виконується, а результат зберігається в кеші під цим ключем.
* Наступні виклики `wrapper` з тим самим набором аргументів повернуть результат із кешу, уникаючи повторного виконання обчислень.

Мемоізація може значно покращити продуктивність функцій, які виконують дорогі обчислення.
Разом з тим може збільшитись використання пам'яті, оскільки результати зберігаються в кеші.
s