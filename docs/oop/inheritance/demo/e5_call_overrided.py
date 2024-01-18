class Person:
	def __init__(self, name):
		self.name = name
	def say_hello(self):
		print('Привіт! Я ', self.name)

obj = Person('Дмитро')
obj.say_hello()
	
class Citizen(Person):
	def say_hello(self):
		Person.say_hello()
		print('Я громадянин України')
	
class Employee(Person):
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
	def say_hello(self):
		print('Привіт! Я ', self.name)
		print('Моя зарплата', self.salary)

e = Employee('Дмитро', 120)
e.say_hello()



class Animal:
	def __init__(self):
		self.can_run = False
		self.can_fly = False

class Horse(Animal):
	def __init__(self):
		super().__init__()
		self.can_run = True

class Eagle(Animal):
	def __init__(self):
		super().__init__()
		self.can_fly = True

class Pegasus(Horse, Eagle):
	pass

p = Pegasus()
p.can_run
p.can_fly

