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

@bread
@salad
def stake():
	print("М'ясо")

stake()

#######################

@salad
@bread
def stake():
	print("М'ясо")
	
stake()