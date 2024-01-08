class SomeClass:
	def i(self):
		print('instance method called', self)
	@classmethod
	def c(cls):
		print('class method called', cls)
	@staticmethod
	def s():
		print('static method called')
		
obj = SomeClass()
# SomeClass.i()
SomeClass.c()
SomeClass.s()

obj.i()
obj.c()
obj.s()

###################

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_tuple(cls, coords):
        return cls(coords[0], coords[1])
        
###################

p1 = Point(1,2)
p2 = Point.from_tuple((3,4))

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	@classmethod
	def from_string(cls, string):
		parts = string.split(',')
		name_str = parts[0]
		age_str = parts[1].strip()
		return cls(name=name_str, age=int(age_str))
		
	@staticmethod
	def is_adult(age):
		return age >= 18

p = Person('Jane', 25)
p = Person.from_string('Jane, 35')
r = Person.is_adult(age=25)


#########

d = dict.fromkeys('abc')