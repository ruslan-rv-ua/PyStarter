from dataclasses import dataclass
from typing import Optional

@dataclass
class Person:
    name: str
    age: int
    # email: Optional[str] = None
    
p = Person('Alice', 25)
# p2 = Person('Alice', "email")
p2 = Person('Alice', 25)
r = p == p2

@dataclass(frozen=True)
class POI:
    lat: float
    lon: float
    name: str
    x=1
    
p = POI(name='WC', lat=1.1, lon=2.2)
p.lat = 3
    
