from copy import deepcopy

m1 = [[0]]
m2 = m1
m1[0][0] = 42

m1 = [[0]]
m2 = deepcopy(m1)
m1[0][0] = 42

a=[None]
a[0]=a

b=deepcopy(a)
