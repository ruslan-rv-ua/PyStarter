def gift_function():
	print('Я — подарунок!')

gift_function()

'''
def wrap_function(gift_to_wrap_function):
	print('Я — святкова обгортка! Я обгорну подарунок.')
	gift_to_wrap_function()
	print('Подарунок обгорнуто!')

wrap_function(gift_function)

'''

def decorator_function(gift_to_wrap_function):
	def wrap_function():
		print('Я — святкова обгортка! Я обгорну подарунок.')
		gift_to_wrap_function()
		print('Подарунок обгорнуто!')	
	return wrap_function

decorated_gift_function = decorator_function(gift_function)

print()
print()
decorated_gift_function()
print()
gift_function()

print()
print()
# gift_function = decorator_function(gift_function)
# gift_function()

print()
print()
def gift_iphone():
	print('Я — айфон!')

gift_iphone = decorator_function(gift_iphone)

@decorator_function
def gift_iphone():
	print('Я — айфон!')
	
gift_iphone()










def bounded_min(first, *args, lo=float('-inf'), hi=float('inf')):
	res = hi
	for arg in (first,) + args:
		if arg < res and lo < arg < hi:
			res = arg
			