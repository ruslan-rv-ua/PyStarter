class Person:
    def __init__(self, name):
        print('Виклик ініціалізатора класа Person')
        self.name = name
    def person_method(self):
        print('Це метод з класа Person')
        print(f'У екземпляра класа Person є атрибут {self.name=}')

class Employee(Person):
    def employee_method(self):
        print('Це метод з класа Employee')
        print(f'У екземпляра класа Employee є атрибут {self.name=}')

class Manager(Employee):
    pass


e = Employee('Bob')
e.person_method()
e.employee_method()
r = e.name



#####################
print('\n'*5)

class Person:
    def __init__(self, name):
        print('Виклик ініціалізатора класа Person')
        self.__name = name
    def person_method(self):
        print('Це метод з класа Person')
        print(f'У екземпляра класа Person є атрибут {self.__name=}')

class Employee(Person):
    def employee_method(self):
        print('Це метод з класа Employee')
        print(f'У екземпляра класа Employee є атрибут {self.__name=}')

class Manager(Employee):
    pass

e = Employee('Bob')
e.person_method()
# e.employee_method()
