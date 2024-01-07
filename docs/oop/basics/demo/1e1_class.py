class Person:
    print('Homo Sapiens')

class Person:
    name = 'Homo Sapiens'
    def info():
        print(Person.name)

        
r = Person.name
Person.info()

p = Person()
# type(p)

#### attrs

s=p.name

p.name = 'Jane'
r=p.name
c=Person.name

#### methods

# p.info()
# p.info() == Person.info(p)
# l.append(42) == list.append(l, 42)

class Person:
    name = 'Homo Sapiens'
    def info(self):
        print(self.name)

p=Person()
p.info()
p2=Person()
p2.name=42
p2.info()
