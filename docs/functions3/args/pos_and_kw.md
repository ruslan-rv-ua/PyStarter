---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

# Параметри і аргументи функцій

Викликаючи функцію, ми можемо передавати їй наступні типи аргументів:

* позиційні аргументи (positional arguments)
* іменовані аргументи (keyword arguments)
* опціональні аргументи (default arguments)
* аргумети довільної довжини (variable-length argumens)


## Позиційні аргументи

Коли викликаємо функцію фактичні параметри заміщують формальні у тому порядку, у якому їх вказано.

	:::python
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

	:::python
	>>> product_info(price=2, name='Pen', color='blue')
	Product: Pen
	Color: blue
	Price: 2
	>>>

При викликах функцій можна одночасно використовувати як позиційні, так і іменовані аргументи. Спочатку треба вказати певну кількість позиційних аргументів, які будуть заміщати відповідні їм по порядку параметри, а потім для усіх аргументів, що залишились, вказуємо іменовані аргументи у довільному порядку:

	:::python
	>>> product_info('Pen', price=2, color='blue')
	Product: Pen
	Color: blue
	Price: 2
	>>>

У прикладі вище перший аргумент буде відповідати параметру функції `name`, інші ж аргументи ми вказали з іменами параметрів.

Спроба вказати позиційний аргумент після іменованих призведе до відповідної помилки:

	:::python
	>>> product_info(price=2, color='blue', 'Pen')
	  File "<stdin>", line 1
	SyntaxError: positional argument follows keyword argument
	>>>
