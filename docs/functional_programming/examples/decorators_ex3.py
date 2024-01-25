def ones(func):
	def wrapper(*args, **kwargs):
		if not wrapper.called:
			wrapper.called = True
			func(*args, **kwargs)
	wrapper.called = False
	return wrapper
	
@ones
def load_data():
	print('Data loaded!')
	
for i in range(5):
	load_data()

	
################
'''
Мемоізація — збереження результатів виконання функції для запобігання надмірних обчислень.
'''

def memoized(func):
	def wrapper(*args, **kwargs):
		key = str(args) + str(sorted(tuple(kwargs.items()) ) )
		if key not in wrapper.cache:
			wrapper.cache[key] = func(*args, **kwargs)
		return wrapper.cache[key]
	wrapper.cache = {}
	return wrapper

@memoized
def f(n):
	s = ''
	for i in range(n):
		s += ' '
	return s
	
f(10**7)
print('done')
f(10**7)
print('done')
f(10**7)
print('done')











