---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

# Документування функцій

Оскільки у мовах програмування, у тому числі Python, існує велика кількість вбудованих та третьосторонніх модулів, то пам'ятати їх усі, у тому числі і їх функціонал, неможливо. 

## Need help?

Інтерпретатор Python надає чудову можливість отримати вбудованими засобами довідку або документацію практичино до усього, до чого вона тільки існує, за допомогою вбудованої функції:

	help()

Якщо функція викликається без аргументів, довідкова система запускається у інтерактивному режимі.
Якщо функції передано символьний рядок, то виконується спроба інтерпретувати її як ім'я модуля, функції, класу, метода або розділу документації, після чого довідка виводиться у консоль. Якщо ж функції передано об'єкт будь-якого іншого типу, довідка герерується по даним цього об'єкта (docstring).

	>>> help(print)
	Help on built-in function print in module builtins:

	print(...)
		print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

		Prints the values to a stream, or to sys.stdout by default.
		Optional keyword arguments:
		file:  a file-like object (stream); defaults to the current sys.stdout.
		sep:   string inserted between values, default a space.
		end:   string appended after the last value, default a newline.
		flush: whether to forcibly flush the stream.

	>>>

Функцію `help()` використовують, в основному, у інтерактивному режимі інтерпретатора.

## docstring

Але звідки ж функція `help()` бере дані документації?

Під час написання коду до практично усіх сутностей Python (функція, метод, клас, модуль) ми одразу ж можемо створювати документацію. Робиться це за допомогою docstring.

*docstring* — це "особливий вид" коментаря. 
Перший коментар, що стоїть на самому початку модуля, функції та ін. і є docstring, або *рядком документації*.

Основні відміни docstring від звичайних коментарів:

- до рядків документації можна отримати доступ під час виконання програми
- рядки документації зберігаються у байт-коді
- до рядків документації мають доступ інтерпретатор, середовище розробки

Напряму доступ до рядків документації можна отримати через атрибут (поле) `__doc__` відповідних об'єктів.

	>>> print(print.__doc__)
	print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

	Prints the values to a stream, or to sys.stdout by default.
	Optional keyword arguments:
	file:  a file-like object (stream); defaults to the current sys.stdout.
	sep:   string inserted between values, default a space.
	end:   string appended after the last value, default a newline.
	flush: whether to forcibly flush the stream.
	>>>

При роботі з інтерпретатором у інтерактивному режимі зручно використовувати функцію `help()` 
для отримання швидкої довідки.

## Конвенції

Є декілька стилів для створення docstring в Python. 
Найбільш поширені — Google Style Docstrings та NumPy Style Docstrings. 

Основні риси стилю Google Style Docstrings:

- Використовує один рядок для короткого опису.
- Деталі про аргументи та повернені значення розміщені у блоках "Args" та "Returns".
- Інші розділи, такі як "Raises", також можуть використовуватися для виняткових ситуацій.

Приклад. Оголосимо функцію і одразу ж створимо до неї документацію:

	def calculate_rectangle_area(width, height):
		"""Calculate the area of a rectangle.

		Args:
			width (float): The width of the rectangle.
			height (float): The height of the rectangle.

		Returns:
			float: The area of the rectangle, calculated as width * height.
		"""
		return width * height

Тепер можемо подивитись довідку до створеної функції:

	>>> help(calculate_rectangle_area)
	Help on function calculate_rectangle_area in module __main__:

	calculate_rectangle_area(width, height)
		Calculate the area of a rectangle.

		Args:
			width (float): The width of the rectangle.
			height (float): The height of the rectangle.

		Returns:
			float: The area of the rectangle, calculated as width * height.

	>>>

Документування прийнято виконувати англійською мовою. 
Багато проектів мають відкритий код, доступні у Вебі, їх вивчають і модифікують програмісти з різних країн. 
Використання однієї мови дозволяє їм розуміти один одного. 
Тому професійний програміст має володіти англійською хоча б на початковому рівні. 
Google Translate – теж варіант. 

---

Написання документації, так само як і коментарів до початкового коду, є дуже важливим! 
Основне призначення коментарів – пояснити що робить код, як він працює. Основне призначення рядків документації – коротко описати в цілому для чого призначено об'єкт, які аргументи приймає, і що повертає. 

Супроводжуйте ваші функції якісною документацією і програмісти, котрі будуть працювати з вашим кодом після вас, будуть вдячні вам.


## Завдання

1. Скориставшись функцією `help()` ознайомтесь з документацією тих сутностей Python, що вас цікавить найбільше на даний момент. 
1. Спробуйте вивчити документацію до функції `help()` 
