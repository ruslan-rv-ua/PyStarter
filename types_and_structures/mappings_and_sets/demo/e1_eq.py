class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    #def __eq__(self, other):
        #return self.name == other.name and self.age == other.age
        
# p1 = Person('Alice', 25)
# p2 = Person('Alice', 25)
# p2 = Person('Alice', 30)
# e = p1 == p2
r = Person('Alice', 25) == Person('Alice', 25)
# students = [p1, p2]
r = Person('Alice', 25) in [Person('Alice', 25)]
