class Person:
    def __init__(self, name):
        self.name = name
    def hello(self):
        print(f'Я — {self.name}')

class Employee(Person):
    def salary(self):
        print('Я отримую зарплатню')

class Manager(Employee):
    def salary(self):
        print('Я отримую підвищену зарплатню')
    def info(self):
        print('Я можу керувати іншими')


m = Manager('Дмитро')
m.hello()
m.salary()
m.info()


# Manager.__mro__
# Manager.mro()
print(' - '.join(c.__name__ for c in Manager.mro()))

r = isinstance(m, Manager)
isinstance(m, Employee)
isinstance(m, object)
isinstance(m, str)
isinstance(Person('Bob'), Manager)

isinstance(m, (Employee, Person))
isinstance(m, (Employee, object))
isinstance(m, (Employee, list))
isinstance(m, (dict, list))
