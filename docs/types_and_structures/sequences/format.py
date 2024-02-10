class Temp:
    def __str__(self):
        return 'str method'
    def __repr__(self):
        return 'repr method'
    def __format__(self, format_spec):
        return 'format method'
		
obj = Temp()
print('{}'.format(obj))
print('{!s}'.format(obj))
print('{!r}'.format(obj))
