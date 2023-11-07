---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

# Інструкція return

Інструкція "return" використовується 
для *повернення* з функції, 
тобто для припинення її роботи 
і виходу з неї. 

	:::python
	def say_hello(name):
		if name == "Петя":
			return
		print('Hello,', name)
	say_hello('Вася')
	say_hello('Петя')
	
Результат:

	Hello, Вася
	>>>

Після return можна вказати вираз, 
і значення цього виразу функція поверне 
у те місце, звідки вона була викликана:

	:::python
	def my_max(a, b):
		if a > b:
			return a
		elif b > a:
			return b
		else:
			return 'equal'
	m = my_max(3, 5)
	print(m)
	print(my_max(5,3))
	print(my_max(5,5))
	
Отримаємо:

	5
	5
	equal
	>>>

Зауважте, що return без вказання значення що повертається 
еквівалентно виразу "return None". 

	:::python
	def positive(a):
		if a <= 0:
			return
		return 'yes'
	print(positive(2))
	print(positive(0))

Результат:

	yes
	None
	>>>

Якщо явно не вказано return, 
то він усе одно присутній у кожній функції неявно,
у самому її кінці:

	:::python
	def f():
		print('It works!')
	a = f()
	print(a)

Результат:

	It works!
	None
	>>>
