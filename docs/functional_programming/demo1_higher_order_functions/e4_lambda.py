def add(x, y):
	return x + y
	
add = lambda x, y: x + y

(lambda x, y: x + y)(5, 7)

hello = lambda name, time='morning': f'Good {time}, {name}'
r=hello('Jane')
r=hello('Jane', 'afternoon')

func = lambda *args: args
r=func(1, 2, 3, 4)

m = lambda x, y: x if x < y else y
r=m(1,3)

#####################################

functions = [
	lambda x: x**2,
	lambda x: x**3,
	lambda x: x**4,
]

for function in functions:
    print(function(2))

d = {
	'add': lambda x, y: x + y,
	'mul': lambda x, y: x * y
}
op = dict(
    add = lambda x, y: x + y,
    mul = lambda x, y: x * y
)

r1 = op['add'](5, 5)
r2 = op['mul'](5, 5)

##################################

from typing import NamedTuple

class Person(NamedTuple):
    name: str
    age: int

persons = [
    Person(name="Борис Петренко", age=25),
    Person(name="Петро Бабенко", age=30),
    Person(name="Марія Сидоренко", age=35),
    Person(name="Олена Василенко", age=40),
    Person(name="Андрій Коваленко", age=45),
    Person(name="Наталія Мельник", age=50),
    Person(name="Сергій Лисенко", age=55),
    Person(name="Тетяна Шевченко", age=60),
    Person(name="Юрій Козак", age=65),
    Person(name="Оксана Литвин", age=70),
    Person(name="Ірина Павленко", age=75),
    Person(name="Володимир Кравченко", age=80),
]

# sort by last name
l = sorted(persons, key=lambda person:person.name.split()[-1])
print('\n'.join(person.name for person in l))

# get 3 oldest
l = sorted(persons, key=lambda person:person.age, reverse=True)[:3]
print('\n'.join(str(person) for person in l))

