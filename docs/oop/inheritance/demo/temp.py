class Person:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        print(f'Привіт! Я {self.name}.')

class Citizen(Person):
    def say_hello(self):
        super().say_hello()
        print('Я громадянин України')
        
class Employee(Citizen):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary
    def say_hello(self):
        super(Employee, self).say_hello()
        print('Моя зарплата', self.salary)

e = Employee('Борис', 1000)
e.say_hello()