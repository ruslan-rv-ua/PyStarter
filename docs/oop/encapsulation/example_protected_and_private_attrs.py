class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
p = Person('Alice', -35)

class Person:
	def __init__(self, name, age):
		self.set_age(age)
	def get_age(self):
		return self._age
	def set_age(self, age):
		assert age >= 0
		self._age = age
		
p = Person('Alice', 25)

# property(fget, fset, fdel, doc)
class Person:
	def __init__(self, name, age):
		self._age = age
	def get_age(self):
		return self._age
	def set_age(self, age):
		assert age >= 0
		self._age = age
	age = property(get_age, set_age, doc='Age, full years')
	
p = Person('Alice', 25)

class Person:
	def __init__(self, name, age):
		self.age = age
	@property
	def age(self):
		return self._age
	@age.setter
	def age(self, age):
		assert age >= 0
		self._age = age

p = Person('Alice', 25)

