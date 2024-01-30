from warnings import warn

class IncorrectNameWarning(UserWarning):
	pass
	
class Person:
	def __init__(self, name):
		if len(name.split()) > 3:
			warn(
				'Name maybe incorrect:' + name,
				IncorrectNameWarning,
				stacklevel=2
			)
		self._name = name
	@property
	def name(self):
		return self._name
		
		
p = Person('Остап Сулейман Берта Марія Бендер')

#############################

from warnings import warn

class Depricated(UserWarning): pass

def f():
	# warn(f"Function 'f()' depricated", Depricated, stacklevel=2)
	warn(f"Function 'f()' depricated")
	
for _ in range(5):
	f()
