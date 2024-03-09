### Декорування класів

Декорувати можна не лише функції, але і класи. 
Реалізуємо декоратор, 
який додає до класа метод для представлення класа у вигляді символьного рядка: 

	:::python
	def auto_str_class(any_class):
		def str(self):
			variables = (f'{key}={value!r}' for key, value in vars(self).items())
			return f'{any_class.__name__}({", ".join(variables)})'
		
		any_class.__str__ = str
		return any_class

Тепер декоровані класи можуть детальнло розказати про себе:

	:::python
	>>> @auto_str_class
	... class Person:
	...     def __init__(self, name, age):
	...         self.name = name
	...         self.age = age
	...
	>>> p = Person('Jane', 26)
	>>> print(p)
	Person(name='Jane', age=26)
	>>>
