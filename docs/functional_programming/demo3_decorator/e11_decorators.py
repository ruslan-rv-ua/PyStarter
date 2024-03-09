def gift():
	print('Подарунок.')

gift()

def wrapper():
	print('Я — святкова обгортка! Я обгорну подарунок.')
	gift()
	print('Подарунок обгорнуто!')

wrapper()

print()


def decorator(gift):
	def wrapper():
		print('Я — святкова обгортка! Я обгорну подарунок.')
		gift()
		print('Подарунок обгорнуто!')	
	return wrapper

# decorated_gift = decorator(gift)
# decorated_gift()
# gift()

gift = decorator(gift)
# gift()

print()

###############

@decorator
def iphone():
	print('Айфон')
	
gift()
