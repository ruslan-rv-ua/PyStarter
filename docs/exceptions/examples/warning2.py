from warnings import warn

class Depricated(UserWarning): pass

def f():
	warn('Function depricated', Depricated, stacklevel=2)
	
for _ in range(5):
	f()
