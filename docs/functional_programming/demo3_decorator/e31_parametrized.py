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

#####################

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

def sandwich(sandwich_with):
	print(sandwich_with)
sandwich = make_sandwich('Хліб')(sandwich)

sandwich('Котлета')

#######################

@make_sandwich('Хліб')
@make_sandwich('Хрін')
def super_sandwich(sandwich_with):
	print(sandwich_with)

super_sandwich("Сало")