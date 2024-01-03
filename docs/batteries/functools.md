# Модуль `functools`

## `reduce()`

Приймає функцію від двох аргументів, послідовность і опціональне початкове значення. 
Обчислює згортання (fold) послідовності як результат послідовного застосування даної функції до поточного значення (так званому акумулятору) і наступному елементу послідовності. Міститься в модулі `functools`. 

Трохи незрозуміло? Розберемось. 

Отже функція `reduce()` приймає три параметри:

- функцію
- ітерабельний об'єкт
- акумулятор

Останній параметр необов'язковий. 
Якщо він відсутній, то в якості акумулятора береться перший елемент послідовності. 

Далі для акумулятора і для кожного наступного елемента послідовності викликається передана функція. 
Результат її дії записується в акумулятор. 
Процес повторюється поки не буде "пройдено" всю послідовність. 

Приклад. 
Є список чисел, треба отримати їх добуток. 

	:::python
	>>> from functools import reduce
	>>> numbers = [1, 2, 3, 4, 5]
	>>> product = reduce(lambda a, x: a*x, numbers)
	>>> product
	120

Функції `reduce()` ми передали анонімну функцію, яка повертає добуток двох чисел. 
Ця функція застосовується спершу до чисел 1 і 2, в результаті отримуємо 2. 
Потім до чисел 2 (попередній результат) і 3 (наступний елемент списка), вийде 6. 
Потім до чисел 6 і 4, і врешті решт до чисел 24 і 5. 

Ще один приклад. 
Є список списків чисел:

	[[1, 2, 3], [4, 5], [6, 7, 8]]
	
Треба отримати один список який міститиме усі числа: 

	[1, 2, 3, 4, 5, 6, 7, 8]
	
За допомогою `reduce()` це можна зробити просто і елегантно: 

	:::python
	>>> nums = [[1, 2, 3], [4, 5], [6, 7, 8]]
	>>> l = reduce(lambda x,y: x+y, nums)
	>>> l
	[1, 2, 3, 4, 5, 6, 7, 8]
	>>>

Ще можна замість анонімної функції використати магічний метод класа `list`:

	:::python
	>>> l = reduce(list.__add__, nums)
	>>> l
	[1, 2, 3, 4, 5, 6, 7, 8]
	>>>

## "Ввічливі" декоратори

Розглянемо нас	тупний приклад:

	:::python
	>>> def decorator(func):
	...     def wrapper():
	...             func()
	...     return wrapper
	...
	>>> @decorator
	... def some_func():
	...     "This is docstring for some_func() function"
	...
	>>> some_func
	<function decorator.<locals>.wrapper at 0x000002167F6DF2F0>
	>>> some_func.__name__
	'wrapper'
	>>> help(some_func)
	Help on function wrapper in module __main__:

	wrapper()

	>>>

Упс... Після декорування функція `some_func` не тільки "забула як її звати", але ще й втратила докстрінги! Це не є добре. Давайте виправимо ситуацію:

	:::python
	>>> def decorator(func):
	...     def wrapper():
	...             func()
	...     wrapper.__name__ = func.__name__
	...     wrapper.__doc__ = func.__doc__
	...     wrapper.__module__ = func.__module__
	...     return wrapper
	...
	>>> @decorator
	... def some_func():
	...     "This is docstring for some_func() function"
	...
	>>> some_func
	<function decorator.<locals>.wrapper at 0x000002167FAB5C80>
	>>> some_func.__name__
	'some_func'
	>>> help(some_func)
	Help on function some_func in module __main__:

	some_func()
		This is docstring for some_func() function

	>>>

Чудово! А щоб при створенні чергового декоратора уникнути рутини можна скористатись вже готовою функцією `wraps` з вбудованого модуля `functools`. І що тут цікаво, що `wraps` теж є декоратором!

	:::python
	>>> from functools import wraps
	>>> def decorator(func):
	...     @wraps(func)
	...     def wrapper():
	...             func()
	...     return wrapper
	...
	>>> def some_func():
	...     "This is docstring for some_func() function"
	...
	>>> some_func.__name__
	'some_func'
	>>> help(some_func)
	Help on function some_func in module __main__:

	some_func()
		This is docstring for some_func() function

	>>>
	
### Шаблони декораторів

Декоратор без параметрів:

	:::python
	from functools import wraps
	def назва_декоратора(функція_що_декорується):
		@wraps(функція_що_декорується)
		def inner(параметри_функції_що_декорується):
			...
			функція_що_декорується(параметри_функції_що_декорується)
			...
		return inner

Декоратор з параметрами:

	:::python
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


### go!
<!-- 
https://habr.com/ru/company/otus/blog/573164/
https://habr.com/ru/company/otus/blog/573164/
Кэшированные атрибуты

Во встроенном пакете functools есть классный декоратор @cached_property, который позволяет кэшировать результат метода и загнать его в атрибут.

Таким образом, при первом обращении к атрибуту производятся вычисления в методе, а при дальнейших берется уже кэшированное значение.

Подобное кэшеирование полезно в случаях, когда в методе производятся вычисления, которые нагружают систему и занимают много времени.

По сути, @cached_property можно сравнить с комбинацией декораторов @property (про это был пост) и @functools.lru_cache (и про это тоже).
-->