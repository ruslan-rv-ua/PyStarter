# itertools.cycle

# itertools.combinations(iterable, r)
from itertools import combinations
keys = list(combinations('0123456789', 2))


# itertools.compress(data, selectors)
from itertools import compress
names = ['Alice', 'Bob', 'Eric', 'Jane']
grades = [1, 0, None, 5]
r = list(compress(names, grades))

