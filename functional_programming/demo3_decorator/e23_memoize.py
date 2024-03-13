from time import perf_counter

def timeit(func):
	def wrapper():
		t = perf_counter()
		func()
		print(f"{func.__name__}: {perf_counter()-t:.8f}")
	wrapper.__name__ = func.__name__
	return wrapper

def memoize(func):
	cache = {}
	def wrapper(*args, **kwargs):
		key = (args, tuple(kwargs.items()))  # унікальний ключ для кешу
		if key not in cache:
			cache[key] = func(*args, **kwargs)
		return cache[key]
	wrapper.__name__ = func.__name__
	return wrapper

@timeit
@memoize
def f1():
	res = ' ' * 10**6

@timeit
@memoize
def f2():
	res = ''
	for i in range(10**6):
		res += ' '

f1()
f2()

f1()
f2()
