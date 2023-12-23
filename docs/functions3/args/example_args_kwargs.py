def all_i_got(*args):
	for arg in args:
		print(arg)
		
all_i_got(1, 2)

def all_i_got(*args, **kwargs):
	for arg in args:
		print(arg)
	for arg in kwargs:
		print(f'{arg} = {kwargs[arg]}')

def all_i_got(first, *args, **kwargs):
	print(first)
	for arg in args:
		print(arg)
	for arg in kwargs:
		print(f'{arg} = {kwargs[arg]}')

		
all_i_got(1, 'text', named=7)
all_i_got(named=7)