n = 0
def f():
	global n
	n += 1
	f()


import sys
# sys.setrecursionlimit(1500)
r=sys.getrecursionlimit()

f()