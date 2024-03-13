import pickle

class Person(object):
    def __init__(self, name, age, sibling=None):
        self.name = name
        self.age = age
        self.sibling = sibling

    def __repr__(self):
        return f'Person({self.name!r}, {self.age!r})'

peter = Person('Петро', 20)
mary = Person('Марійка', 21, peter)
peter.sibling = mary

with open('people.bin', 'wb') as file:  # 'wb' - записуємо бінарний файл!
	pickle.dump([peter, mary], file)
