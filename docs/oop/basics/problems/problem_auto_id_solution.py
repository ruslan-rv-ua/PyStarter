'''Створити клас AutoId.
Кожен новий екземпляр цього класа повинен мати атрибут id зі значенням, яке дорівнює порядку створення цього екземпляра.
Перший створений екземпляр має атрибут id==1.
Другий створений екземпляр має атрибут id==2.
І так далі.
'''

class AutoId:
    # ваш код починається тут
    counter = 0
    
    def __init__(self):
        # AutoId.counter += 1
        # self.__class__.counter += 1
        type(self).counter += 1
        self.id = self.counter
    
# юніт-тести
a = AutoId()
assert a.id == 1
for _ in range(99):
    AutoId()
assert AutoId().id == 101
