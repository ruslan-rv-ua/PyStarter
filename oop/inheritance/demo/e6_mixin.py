class Logger:
    def log(self, message):
        print(f'{self.__class__.__name__}: {message}')

class Person:
    def __init__(self, name):
        self.name = name.title()

class LoggedPerson(Logger, Person):
    pass

p = LoggedPerson('Alice')
p.log('some message')
