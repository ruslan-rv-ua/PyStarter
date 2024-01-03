class Person:
	def __init__(self, name):
		assert name != ''
		self.name = name
	def say_hello(self):
		print('Привіт! Я ', self.name)
		
class Citizen(Person):
	def say_hello(self):
		Person.say_hello(self)
		print('Я громадянин України')


class Employee(Citizen):
	def __init__(self, name, salary):
		super(Employee, self).__init__(name)
		self.salary = salary
	def say_hello(self):
		super(Person, self).say_hello()
		print('Моя зарплата', self.salary)

p = Employee('Дмитро', 120)
p.say_hello()
