def f1():
	res = ' ' * 10**6

def f2():
	res = ''
	for i in range(10**6):
		res += ' '

####################################

from time import perf_counter

def timeit(func):
	def wrapper():
		t = perf_counter()
		func()
		print(f"{func.__name__}: {perf_counter()-t}")
	return wrapper
	
@timeit
def f1():
	res = ' ' * 10**7

@timeit
def f2():
	res = ''
	for i in range(10**7):
		res += ' '

f1()
f2()
