def gift():
	print('Айфон')

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

decorated_gift()
gift()

gift = decorator(gift)
gift()

###############

@decorator
def gift():
	print('Айфон')
	
gift()
			