def double(obj):
	print(f'До: {obj}')
	obj = obj * 2
	print(f'Після: {obj}')

x = 1
x = [1]
double(x)

def append(obj):
	print(f'До: {obj}')
	obj.append(7)
	print(f'Після: {obj}')

x = [1]
append(x)