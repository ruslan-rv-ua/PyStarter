class Base:
	pass
	
class Child(Base):
	pass
	
######################
class SuperBase:
	pass

class Base(SuperBase):
	pass
	
class Child(Base):
	pass
	
# print(issubclass(Child, Base))
r = issubclass(Child, Base)

r = issubclass(Child, (Base, object))

r = Child.__bases__
