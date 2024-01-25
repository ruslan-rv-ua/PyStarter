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
		
		
p = Person('Остап Сулейман Берта Мария Бендер')
