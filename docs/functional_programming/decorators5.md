---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

### "Ввічливі" декоратори

Розглянемо протсий декоратор::

```python
def decorator(func):
    def wrapper():
        func()
    return wrapper
    
@decorator
def simple_function():
    """Docstring for `simple_function()`"""
    pass
```

Дослідимо декоровану функцію:

    >>> simple_function.__doc__
    >>> simple_function.__name__
    'wrapper'
    >>>

Упс... 
Після декорування функція `simple_func` не тільки "забула як її звати", 
але ще й втратила докстрінги! 
Це не є добре. 
Давайте виправимо ситуацію:

```python
def decorator(func):
	def wrapper():
		func()
	wrapper.__name__ = func.__name__
	wrapper.__doc__ = func.__doc__
	return wrapper

@decorator
def simple_function():
	"""Docstring for `simple_function()`"""
	pass
```

Перевіримо:

    >>> simple_function.__doc__
    'Docstring for `simple_function()`'
    >>> simple_function.__name__
    'simple_function'
    >>>

Чудово! 

А щоб при створенні чергового декоратора уникнути рутини можна скористатись вже готовою функцією `wraps` з модуля `functools`. 
І що тут цікаво, що `wraps` теж є декоратором!

```python
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper():
        func()
    return wrapper
    
@decorator
def simple_function():
    """Docstring for `simple_function()`"""
    pass
```

Тепер перевіримо:

    >>> simple_function.__doc__
    'Docstring for `simple_function()`'
    >>> simple_function.__name__
    'simple_function'
    >>>


Отже при створенні декораторів можна використовувати певні шаблони. 

Декоратор без параметрів:

	from functools import wraps
	def назва_декоратора(функція_що_декорується):
		@wraps(функція_що_декорується)
		def inner(параметри_функції_що_декорується):
			...
			функція_що_декорується(параметри_функції_що_декорується)
			...
		return inner

Декоратор з параметрами:

	from functools import wraps
	def назва_декоратора(параметри_декоратора):
		def decorator(функція_що_декорується):
			@wraps(функція_що_декорується)
			def inner(параметри_функції_що_декорується):
				...
				функція_що_декорується(параметри_функції_що_декорується)
				...
			return inner
		return decorator



<!-- 
https://habr.com/ru/company/otus/blog/573164/
https://habr.com/ru/company/otus/blog/573164/
Кэшированные атрибуты

Во встроенном пакете functools есть классный декоратор @cached_property, который позволяет кэшировать результат метода и загнать его в атрибут.

Таким образом, при первом обращении к атрибуту производятся вычисления в методе, а при дальнейших берется уже кэшированное значение.

Подобное кэшеирование полезно в случаях, когда в методе производятся вычисления, которые нагружают систему и занимают много времени.

По сути, @cached_property можно сравнить с комбинацией декораторов @property (про это был пост) и @functools.lru_cache (и про это тоже).
-->
