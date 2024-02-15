# __bool__()
# bool(x)
# False = False, None, 0, len()==0

# Truthy / Falsy
def print_even(data):
	if not data: # if len(data) == 0:
		raise ValueError()
	for value in data:
		if not value % 2: # if value % 2 == 0:
			print(value)
			
print_even([1,2,3,4])
# print_even([])

def f(l=None):
    if not l:
        print('None')
    else:
        print('list')
f([])


#########################
# x or y # y якщо bool(x) is False, інакше x
r = 'me' or 'you'
# x and y # x якщо bool(x) is False, інакше y
r = 'me' and 'you'
r = 'me' and None
r = None and 'you'
# not x	True якщо bool(x) is False, інакше False

################################
# "Ліниві" логічні обчислення
l = ['yes', 1]
l.pop() or l.pop()

l = ['yes', 0]
l.pop() and l.pop()

#####################
# Згортання операцій порівняння

l = [1, 2, 3]
# l = [3, 2, 1]

# v1 < v2 == v3
# v1 < v2 and v2 == v3
r = l.pop() < l.pop() < l.pop()


########################################
# compare
[1,2] == '12'
# [1,2] > '12'

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __eq__(self, other):
        return self.age == other.age
    def __lt__(self, other):
        return self.age < other.age
        
p1 = Person('Alice', 35)
p2 = Person('Bob', 39)

