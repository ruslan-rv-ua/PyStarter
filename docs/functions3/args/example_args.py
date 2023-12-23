def product_info(name, color, price):
	print('Product:', name)
	print('Color:', color)
	print('Price:', price)

product_info('Pen', 'blue', 2)
product_info(2, 'Pen', 'blue')

product_info(price=2, name='Pen', color='blue')
product_info('Pen', price=2, color='blue')
product_info(price=2, color='blue', 'Pen')



def product_info(name, color='blue', price=7):
	print('Product:', name)
	print('Color:', color)
	print('Price:', price)

product_info('Pen')
product_info('Pen', 'red')
product_info('Pen', price=5)


def change_list(lst=[]):
	lst.append(1)
	return lst
	
l = change_list()
l = change_list([2,4])
l = change_list()

def change_list(lst=None):
	if lst is None:
		lst = []
	lst.append(1)
	return lst