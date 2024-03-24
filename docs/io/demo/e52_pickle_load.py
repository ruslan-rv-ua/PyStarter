import pickle

class Person(object):
    def __init__(self, name, age, sibling=None):
        self.name = name
        self.age = age
        self.sibling = sibling

    def __repr__(self):
        return f'Person({self.name!r}, {self.age!r})'

with open('people.bin', 'rb') as file:
    data = pickle.load(file)

