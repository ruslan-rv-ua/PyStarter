class Person:
	def __init__(self, name, age):
		self._name = name
		self._age = age
		
p = Person('Alice', 35)
print(p._age)


class Person:
	def __init__(self, name, age):
		self.__name = name
		self.__age = age
		
p = Person('Alice', 35)
p.__age = 0
print(p.__age)
print(p._Person__age)
