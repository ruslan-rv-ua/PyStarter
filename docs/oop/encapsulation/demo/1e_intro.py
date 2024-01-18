class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f'Person({self.name}, {self.age})'

p = Person('Alice', 35)
p.age = -25
