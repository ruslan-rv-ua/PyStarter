class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #def __repr__(self):
        #return f'Person(name={repr(self.name)}, age={self.age})'
        # return f'Person(name={self.name!r}, age={self.age!r})'
    #def __str__(self):
        #return f'{self.name}, {self.age} years old.'

p = Person('Alice', 25)
print(p)
print(repr(p))