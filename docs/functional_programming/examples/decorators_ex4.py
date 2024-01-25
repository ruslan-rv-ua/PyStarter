def div(a, b):
	return a / b

# div(1, 0)

def smart_div(func):
	def wrapper(a, b):
		print("I am going to divide",a,"and",b)
		if b == 0:
			print("Oops! cannot divide")
			return
		return func(a, b)
	return wrapper

#################

def works_for_all(func):
	def wrapper(*args, **kwargs):
		print('I got next parameters:', args, kwargs)
		return func(*args, **kwargs)
	return wrapper
		
@works_for_all
def f(a, b):
	pass
	
f()

	
###################


def bread(func):
	def wrapper():
		print('Хліб')
		func()
		print('Хліб')
	return wrapper

def salad(func):
	def wrapper():
		print('Зеленина')
		func()
		print('Зеленина')
	return wrapper



# @bread
# @salad

def stake():
	print("М'ясо")
	
stake = bread(salad(stake))
	
stake()