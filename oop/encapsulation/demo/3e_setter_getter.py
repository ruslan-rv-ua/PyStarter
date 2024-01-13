class Person:
    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)
    def get_name(self):
        return self._name
    def set_name(self, name):
        if name == "":
            raise ValueError(f'"name" can not be empty string')
        self._name = name
            
    def get_age(self):
        return self._age
    def set_age(self, age):
        if age < 1:
            raise ValueError(f'age must be > 0, but {age!r} given')
        self._age = age
            
p = Person('Alice', 35)
# p = Person('', 35)
# p = Person('Alice', -35)
r=p.get_age()
# p.set_age(-1)
