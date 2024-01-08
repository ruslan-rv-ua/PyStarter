class Person:
    """Simple Person class."""
    
    def __init__(self, name, age):
        """Initializer.
        
        Args:
            name (str): Person's name
            age (int): Person's age, full years
        """
        self.name = name
        self.age = age
        
    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, name):
        if name != "":
            self._name = name
        else:
            raise ValueError(f'"name" can not be empty string')
    
    @property
    def age(self):
        "Person's age, full years"
        return self._age
        
    @age.setter
    def age(self, age):
        if age > 0:
            self._age = age
        else:
            raise ValueError(f'age must be > 0, but {age!r} given')

    
p = Person('Alice', 35)
