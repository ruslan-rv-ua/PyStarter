---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

# Декоратори з параметрами

Давайте напишемо декоратор, який буде готувати нам сендвічі:

```python
def make_sandwich(func):
	def wrapper():
		print('Хліб')
		func()
		print('Хліб')
	return wrapper

@make_sandwich
def sandwich(sandwich_with):
	print(sandwich_with)
```

Приготуємо один:

	>>> sandwich("М'ясо")
	Хліб
	М'ясо
	Хліб
	>>>

Непогано. 
Але як щодо ситуації, коли для приготування сендвіча ми захочемо використовувати не хліб, а, припустимо, тости? 
Напрошується ідея повідомити декоратору що ми хочемо використовувати в якості "обгортки" нашого сендвіча, тобто передати декоратору якісь параметри.

Отже, декоратор приймає свої параметри, але потім він ще має прийняти функцію, яку має декорувати, а потім ще й аргументи декорованої функції. 
Таким чином нам доведеться зробити аж 3 функції:

```python
def make_sandwich(sandwich_cover):
	def decorator(func):
		def wrapper(sandwich_with):
			print(sandwich_cover)
			func(sandwich_with)
			print(sandwich_cover)
		return wrapper
	return decorator
```

Ось рецепт приготування сендвічів з тостами:

```python
@make_sandwich('Тост')
def sandwich(sandwich_with):
	print(sandwich_with)
```

Готуємо сендвічі по цьому рецепту:

	>>> sandwich("Ковбаса")
	Тост
	Ковбаса
	Тост
	>>> sandwich("Сало")
	Тост
	Сало
	Тост
	>>>

Функція `make_sandwich` приймає в якості параметра "обгортку" для сендвіча `sandwich_cover` і повертає функцію `decorator` яка, як і раніше, приймає тільки функцію що треба декорувати і повертає свою внутрішню функцію `wrapper`, яка у свою чергу приймає аргументи декорованої функції `func`.

Те ж саме можна написати "без магії":

```python
def sandwich(sandwich_with):
	print(sandwich_with)
sandwich = make_sandwich('Хліб')(sandwich)
```

Готуємо:

	>>> sandwich('Котлета')
	Хліб
	Котлета
	Хліб
	>>>

З декораторів з параметрами теж можна будувати ланцюжки:

```ython
@make_sandwich('Хліб')
@make_sandwich('Хрін')
def super_sandwich(sandwich_with):
	print(sandwich_with)
```

Тепер приготуємо "справжній український сендвіч" 😀:

	>>> super_sandwich("Сало")
	Хліб
	Хрін
	Сало
	Хрін
	Хліб
	>>>

Сама зовнішня функція `make_sandwich()` як би виготовляэ декоратори з потрібними властивостями. 
Такі функції називають "фибриками декораторів".




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

```python
class sandwich_cover:
	def __init__(self, cover):
		self._cover = cover
		
	def __call__(self, func):
		def wrapper(sandwich_with):
			print(self._cover)
			func(sandwich_with)
			print(self._cover)
		return wrapper
```

Рецепт "класного" суперсендвіча:

```python
@sandwich_cover('Тост')
@sandwich_cover('Хрін')
def super_sandwich(sandwich_with):
	print(sandwich_with)
```

Приготуємо "класний" сендвіч:
		
	>>> super_sandwich("Сало")
	Тост
	Хрін
	Сало
	Хрін
	Тост
	>>>

Код виглядає набагато читабельнішим. 
Залишилось лише змиритись з назвою класа з маленької букви, 
або ж з назвою декоратора з великої 😊.
