from abc import ABC, abstractmethod

class Employee(ABC):
# class Employee():
    def __init__(self, name):
        self._name = name
    def say_hello(self):
        print(f'Я {self._name}')
    @abstractmethod
    def work(self):
        # print('Я типу щось там роблю')
        raise NotImplementedError()

class Programmer(Employee):
    def work(self):
        print('Пишу код')

class Tester(Employee):
    def work(self):
        print('Тестую')
        
class SonOfBoss(Employee):
    def work(self):
        super().work()

p = Programmer('Дмитро')
p.work()
c = SonOfBoss('Вася')
c.work()
