def outer():
	message = 'Hi there!'
	def inner():
		print(message)
	return inner

f = outer()
f()
	
def outer(message):
	def inner():
		print(message)
	return inner


hello_func = outer('Hello')
bye_func = outer('Bye')
hello_func()
bye_func()


def make_quadratic(a, b, c):
	def quadratic(x):
		return a*x*x + b*x + c
	return quadratic
	
f1 = make_quadratic(1, 0, 0) # f(x) = x*x
f1(5)
