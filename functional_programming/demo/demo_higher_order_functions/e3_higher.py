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

students = [
    {"name": "Аліса", "age": 20},
    {"name": "Дмитро", "age": 18},
    {"name": "Петро", "age": 22},
]

# список імен по віку

def get_age(student):
    return student['age']
r = [student['name'] for student in sorted(students, key=get_age)]

