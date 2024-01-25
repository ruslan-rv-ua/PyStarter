def gift():
	print('Я — подарунок!')

gift()

'''
def wrap(gift_to_wrap):
	print('Я — святкова обгортка! Я обгорну подарунок.')
	gift_to_wrap()
	print('Подарунок обгорнуто!')

wrap(gift)

'''

def decorator(gift_to_wrap):
	def wrap():
		print('Я — святкова обгортка! Я обгорну подарунок.')
		gift_to_wrap()
		print('Подарунок обгорнуто!')	
	return wrap

decorated_gift = decorator(gift)

print()
print()
decorated_gift()
print()
gift()

print()
print()
# gift = decorator(gift)
# gift()

print()
print()
def gift_iphone():
	print('Я — айфон!')

gift_iphone = decorator(gift_iphone)

@decorator
def gift_iphone():
	print('Я — айфон!')
	
gift_iphone()










def bounded_min(first, *args, lo=float('-inf'), hi=float('inf')):
	res = hi
	for arg in (first,) + args:
		if arg < res and lo < arg < hi:
			res = arg
			