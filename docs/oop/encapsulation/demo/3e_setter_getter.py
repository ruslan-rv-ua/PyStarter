class Person:
    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)
    def get_name(self):
        return self._name
    def set_name(self, name):
        if name != "":
            self._name = name
        else:
            raise ValueError(f'"name" can not be empty string')
    def get_age(self):
        return self._age
    def set_age(self, age):
        if age > 0:
            self._age = age
        else:
            raise ValueError(f'age must be > 0, but {age!r} given')
p = Person('Alice', 35)
# p = Person('', 35)
# p = Person('Alice', -35)
print(p.get_age())
p.set_age(-1)
