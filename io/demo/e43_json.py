import json
from typing import NamedTuple

class Person(NamedTuple):
    name: str
    age: int

mary = Person("Мар'яна", 19)

s = json.dumps(mary, ensure_ascii=False)
r = json.loads(s)