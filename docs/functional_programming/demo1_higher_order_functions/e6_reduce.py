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

numbers = [[1, 2, 3], [4, 5], [6, 7, 8]]
l = reduce(lambda l1, l2: l1+l2, numbers)
l = reduce(list.__add__, numbers)

l = reduce(add, numbers)

###########
# factorial
f = reduce(mul, range(1, 4))