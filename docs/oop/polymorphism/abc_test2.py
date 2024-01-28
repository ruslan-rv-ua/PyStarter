from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def say_hello(self):
        pass

class Cow(Animal):
    def say_hello(self):
        print('Му')

class Dog(Animal):
    def say_hello(self):
        print('Гав')

class Cat(Animal):
    def say_hello(self):
        print('Мяу')

c = Cow()
c.say_hello()

d = Dog()
d.say_hello()

c = Cat()
c.say_hello()

