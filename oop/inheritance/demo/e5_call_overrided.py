class Person:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        print(f'Привіт! Я {self.name}.')

p = Person('Дмитро')
p.say_hello()
    
class Citizen(Person):
    def say_hello(self):
        Person.say_hello(self)
        print('Я громадянин України')
        
c = Citizen('Дмитро')
c.say_hello()
    
class Employee(Person):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def say_hello(self):
        Person.say_hello(self)
        print('Моя зарплата', self.salary)

e = Employee('Дмитро', 120)
e.say_hello()



class Animal:
    def __init__(self):
        print('Конструктор Animal')
        self.can_run = False
        self.can_fly = False

class Horse(Animal):
    def __init__(self):
        print('Конструктор Horse')
        super().__init__()
        self.can_run = True

class Eagle(Animal):
    def __init__(self):
        print('Конструктор Eagle')
        super().__init__()
        self.can_fly = True

class Pegasus(Horse, Eagle):
# class Pegasus(Eagle, Horse):
    pass


print('---------------')
r = Pegasus()
print('---------------')
class_ = Animal
# class_ = Horse
class_ = Pegasus
r = class_().can_run
f = class_().can_fly

