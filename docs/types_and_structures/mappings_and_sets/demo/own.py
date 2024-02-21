s={1,2,3}
r=s.pop(4)

from dataclasses import dataclass
@dataclass
#@dataclass(frozen=True)
class Person:
    name: str
    age: int
    
e = Person('Alice', 25) == Person('Alice', 25)
d = {Person('Alice', 25):42}
i = Person('Alice', 25) in d

s={1,2,3}
r=s.pop()