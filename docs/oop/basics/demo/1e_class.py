class NewClass:
    print('це новий клас')
    
class Adder:
    n = 5
    def add(value):
        return Adder.n + value
        
r = Adder.n
r = Adder.add(4)

a = Adder()
# type(a)

#### attrs

r=a.n

a.n = 'number'
r=a.n
c=Adder.n

#### methods

# r=a.add(4)
# a.add() == Adder.add(a)
# a.add(4) == Adder.add(a, 4)

class Adder:
    n = 5
    def add(self, value):
        return self.n + value

a=Adder()
ra=a.add(4)
b=Adder()
b.n='Hello, '
rb=b.add('world')


