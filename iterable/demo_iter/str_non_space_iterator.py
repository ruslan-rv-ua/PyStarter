class Str:
    def __init__(self, string):
        self.string = string
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        while self.index < len(self.string):
            char = self.string[self.index]
            self.index += 1
            if not char.isspace():
                return char
        raise StopIteration

from collections import UserString

class Str2(UserString):
    def __iter__(self):
        self.index = 0
        return self
    def __next__(self):
        while self.index < len(self):
            char = self[self.index]
            self.index += 1
            if not char.isspace():
                return str(char)
        raise StopIteration


s = Str2('a df f\n')
#l = list(s)
print(''.join(s))
