class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def __str__(self):
        return f'{self.name} <{self.email}>'
    def __repr__(self):
        return f'Person(name={repr(self.name)}, email={repr(self.email)})'
        # return f'Person(name={self.name!r}, email={self.email!r})'

p = Person('Alice', 'alice@wonderland.org')
print(p)
print(repr(p))