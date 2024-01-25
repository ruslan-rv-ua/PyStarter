def make_sandwich(func):
	def wrapper(sandwich_with):
		print('Хліб')
		func(sandwich_with)
		print('Хліб')
	return wrapper
	
@make_sandwich
def sandwich(sandwich_with):
	print(sandwich_with)
	
sandwich("М'ясо")

print()
print()

def make_sandwich(sandwich_cover):
	def decorator(func):
		def wrapper(sandwich_with):
			print(sandwich_cover)
			func(sandwich_with)
			print(sandwich_cover)
		return wrapper
	return decorator
	
@make_sandwich('Тост')
def sandwich(sandwich_with):
	print(sandwich_with)
	
sandwich("Ковбаса")

@make_sandwich('Хліб')
def sandwich(sandwich_with):
	print(sandwich_with)
	
# sandwich = make_sandwich('Хліб')(sandwich)
	
sandwich("Сало")


###############
print()
print()
print()


@make_sandwich('Хліб')
@make_sandwich('Хрін')
def super_sandwich(sandwich_with):
	print(sandwich_with)

super_sandwich("Сало")



#####################

print()
print()
print()
print()
print()
print()





def decorator(func):
	def wrapper():
		func()
	return wrapper
	
@decorator
def some_func():
	"This is docstring for some_func() function"
	
def decorator(func):
	def wrapper():
		func()
	wrapper.__name__ = func.__name__
	wrapper.__doc__ = func.__doc__
	wrapper.__module__ = func.__module__
	return wrapper

@decorator
def some_func():
	"This is docstring for some_func() function"	

	
from functools import wraps	
def decorator(func):
	@wraps(func)
	def wrapper():
		func()
	return wrapper
	
def some_func():
	"This is docstring for some_func() function"	

