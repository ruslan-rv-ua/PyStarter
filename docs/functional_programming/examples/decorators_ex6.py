DEBUG = True

def trace(func):
	if not DEBUG:
		return func
	def wrapper():
		print(func.__name__, 'started')
		func()
		print(func.__name__, 'finished')
	return wrapper
	
@trace
def f():
	print('function to trace')
	
f()

DEBUG = False
@trace
def f():
	print('function to trace')

f()
