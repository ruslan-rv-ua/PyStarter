from typing import NamedTuple

class Person(NamedTuple):
    name: str
    age: int
    email: str = ''
    
p = Person('Alice', '26')
