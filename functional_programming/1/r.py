import sys

n = 100000
r = range(n)
r = [f'string{n}' for n in range(n)]

l = list(r)
t = tuple(r)
s = set(r)
d = dict.fromkeys(r)

for o in (l,t,s,d):
    v = sys.getsizeof(o)
    print(type(o).__name__, v)

