''' спеціальний (ad hoc)
int increment(int x) {
    return x + 1;
}

double increment(double x) {
    return x + 1.0;
}

increment(25);
increment(25.0);


override — перевизначити
overload — перевантажити
'''

class WashingMachine:
    def start(self):
        print('Починається процес прання.')
       
class Computer:
    def start(self):
        print('Windows завантажується.')
        
def start(obj):
    obj.start()

for some_device in WashingMachine(), Computer():
    start(some_device)
    some_device.start()

class Duck:
    def quack(self):
        print('Кря!')

class Person:
    def __init__(self, name):
        self.name = name
    def quack(self):
        print('Людина імітує крякання: "Кря!"')

#for any in Duck(), Person('John'):
#   any.quack()

