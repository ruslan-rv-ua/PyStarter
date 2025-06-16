from functools import reduce
from operator import add, mul

numbers = [1, 2, 3, 4, 5]
r = reduce(lambda a, x: a*x, numbers)

### min
m = reduce(lambda n1, n2: n1 if n1<n2 else n2, numbers)
### sum
s = reduce(add, numbers)
s = reduce(add, numbers, 100)
########

numbers = [[], [1, 2, 3], [4, 5], [6, 7, 8]]
l = reduce(lambda l1, l2: l1+l2, numbers)
l = reduce(list.__add__, numbers)

l = reduce(add, numbers)
r1 = sum(reduce(add, numbers))

###########
# factorial
def factorial(n):
    return reduce(mul, range(1, n+1))
f1 = reduce(mul, range(1, 4))
f2 = factorial(3)
