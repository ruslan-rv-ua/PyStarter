def f(x):
    return x + 1
 
def g(function, x):
    return function(x) * function(x)
 
print(g(f, 7))


###############################################

l = ['a', 'e', 'B', 'C']

r1 = sorted(l)

def to_lower(string):
	return string.lower()
	
r2 = sorted(l, key=to_lower)

r3 = sorted(l, key=str.lower)


###########################

l = [5, -2, 10, -8, 3]
r = sorted(l, key=abs)

#########################

l = ['кінь', 'корова', 'селезень', 'баран', 'кіт']
r = sorted(l, key=len, reverse=True)

#########################

from typing import NamedTuple

class Person(NamedTuple):
    name: str
    age: int
    


students = [
    Person(name='Alice', age=30),
    Person(name='Bob', age=25),
    Person(name='Charlie', age=35),
    Person(name='David', age=28),
    Person(name='Eve', age=22),
    Person(name='Frank', age=45),
    Person(name='Grace', age=29),
    Person(name='Heather', age=32),
    Person(name='Isaac', age=40),
    Person(name='Judy', age=37),
]

# список імен по віку

def get_age(student):
    return student.age
r = [student.name for student in sorted(students, key=get_age)]

