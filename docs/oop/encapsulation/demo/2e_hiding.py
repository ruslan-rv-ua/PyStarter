class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    def __repr__(self):
        return f'Person({self._name}, {self._age})'
        
p = Person('Alice', 35)
age = p._age

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def __repr__(self):
        return f'Person({self.__name}, {self.__age})'
        
p = Person('Alice', 35)
age = p._Person__age

# age = p.__age
p.__age = 'twenty two'
age = p.__age
