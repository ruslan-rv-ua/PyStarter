'''Створити клас AutoId.
Кожен новий екземпляр цього класа повинен мати атрибут id зі значенням, яке дорівнює порядку створення цього екземпляра.
Перший створений екземпляр має атрибут id==1.
Другий створений екземпляр має атрибут id==2.
І так далі.
'''

class AutoId:
    # ваш код починається тут
    _counter = 0
    
    def __init__(self):
        self.__class__._counter += 1
        self._id = self._counter
        
    @property
    def id(self):
        return self._id
    
    @classmethod
    @property
    def counter(cls):
        return cls._counter
        
    def __repr__(self):
        return f'<AutoId, id={self.id}>'
        # return f'<{self.__class__.__name__}, id={self.id}>'
        
    
# юніт-тести
a = AutoId()
assert a.id == 1
for _ in range(99):
    AutoId()
assert AutoId().id == 101

c = AutoId.counter
