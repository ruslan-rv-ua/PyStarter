def log_params(func):
	def wrapper(*args, **kwargs):
		print('args:', args)
		print('kwargs:', kwargs)
		return func(*args, **kwargs)
	return wrapper

@log_params
def f(a, b, c):
	print(a, b, c)

f(1, 2, 3)