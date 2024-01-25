class Person:
    species = "Homo sapiens"

    def __init__(self, name):
        self.name = name
        
    def say_hello(self):
        print(f'I am {self.name}')
        
p = Person('Jane')

getattr(p, 'name')
getattr(p, 'age', 24)
getattr(p, 'age')

getattr(Person, 'species')

setattr(p, 'name', 'Alice')
p.name
setattr(p, 'email', 'alice@wonderland.nowhere')
p.email
setattr(Person, 'species', 'Homo neanderthalensis')

delattr(p, 'name')
getattr(p, 'name', 'N/A')
delattr(p, 'phone')


p = Person('Jane')
hasattr(p, 'name')
hasattr(p, 'address')
hasattr(Person, 'species')



exit()


class Person:
    species = "Homo sapiens"

    def __init__(self, name):
        self.name = name
        
    def say_hello(self):
        print(f'I am {self.name}')
        
p = Person('Jane')


p.__dict__['name']
p.__dict__['name'] = 'Alice'
p.name
p.__dict__['age'] = 24
p.age

r = Person.__dict__
Person.__dict__['species']

