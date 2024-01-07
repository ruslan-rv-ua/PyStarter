'''
Завдання розбито на декілька кроків. 
Виконуйте завдання покроково.
Після кожного кроку вивчайте досягнений результат.
1. Реалізуйте клас Rectangle який описує прямокутник із заданими сторонами. 
2. Реалізуйте представлення для екземплярів класа, тобто методи __str__() і __repr__(). 
3. Реалізуйте метод get_area() який повертатиме площу прямокутника.
4. Для метода get_area() створіть docstring. Прочитайте документацію до метода за допомогою help().
5. Вивчіть документацію до класа Rectangle. Які висновки можна зробити?
'''
class Rectangle:
	# ваш код починається тут
	def __init__(self, a, b):
		self.a = a
		self.b = b
	
	def get_area(self):
		'''Returns square of the rectangle.
		'''
		return self.a * self.b
	
	def __repr__(self):
		return f'Rectangle({self.a!r}, {self.b!r})'
	
# не міняйте наступний код, це тести
r = Rectangle(7, 3.0)
print(repr(r))
print(f'Square of {r} is {r.get_area()}')