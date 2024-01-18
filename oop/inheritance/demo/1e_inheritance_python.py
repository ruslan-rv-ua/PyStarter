class Person:
	pass

class Employee(Person):
	pass

class Manager(Employee):
	pass

r = issubclass(Manager, Employee)
issubclass(Manager, Person)
issubclass(Manager, object)
issubclass(Manager, Manager)
issubclass(Employee, Manager)
issubclass(Employee, Person)
issubclass(Person, Employee)
issubclass(str, object)


r = Manager.__bases__

# r = Person.__name__

