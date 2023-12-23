---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

## Опційні аргументи

Деякі параметри функції можна зробити необов'язковими. 
Для цього для них при визначенні функції треба вказати значення за замовчуванням. 
Це значення буде присвоєно параметру якщо ми викликаючи функцію не вкажемо відповідний аргумент:

	:::python
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
	
***Зауважте:*** 
значення за замовчуванням обчислюються і створюються лише один раз, 
а саме при створенні функції! 
У цей момент вони зв'язуються з іменами відповідних параметрів. 

Тому будьте обережними якщо у якості значення за замовчуванням вказуєте мутабельні об'єкти. 

	:::python
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

	:::python
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
	
