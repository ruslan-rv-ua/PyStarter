class Person:
    species = 'Homo Sapiens'
    def info(self):
        print(f"{self.species}: {self.name}")
    
p1 = Person()
p2 = Person()

p1.name ='Jane'
p1.info()
# p2.info()

##############

class Person():
    species = 'Homo Sapiens'
    def __init__(self, name):
        self.name = name
    def info(self):
        print(f"{self.species}: {self.name}")

p1 = Person('Jane')
name = p1.name
# p2 = Person()

class Person():
    def __init__(self, name, email=None):
        self.name = name
        self.email = email
p1 = Person('Jane')
p2 = Person('Alice', 'alice@wonderland.org')

## !!! init -> None