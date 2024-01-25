from time import clock

def f1():
	res = ' ' * 10**6

def f2():
	res = ''
	for i in range(10**6):
		res += ' '

def timeit(func):
	def wrapper():
		t1 = clock()
		func()
		print(clock()-t1)
	return wrapper
	
---
@timeit
def f1():
	res = ' ' * 10**6

@timeit
def f2():
	res = ''
	for i in range(10**6):
		res += ' '

f1()
f2()
