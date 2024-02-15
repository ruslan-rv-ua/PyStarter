from dataclasses import dataclass
from typing import Optional

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

@dataclass
class Person:
    name: str
    age: int
    email: Optional[str] = None
    
p1 = Person('Alice', 25)
# p2 = Person('Alice', "email")
p2 = Person('Alice', 25)
r = p1 == p2
# r = p1 > p2



@dataclass
class Person:
    name: str
    age: int
    email: Optional[str] = None
    # def __eq__(self, other):
        # return self.age == other.age
    def __lt__(self, other):
        return self.age < other.age

p1 = Person('Alice', 25)
p2 = Person('Bob', 35)
r = p1 == p2
r = p1 < p2




@dataclass(frozen=True)
class POI:
    lat: float
    lon: float
    name: str
    x=1
    
p = POI(name='cafe', lat=1.1, lon=2.2)
# p.lat = 3
p.x
