class SuperBase:
	def f1(self):
		print('Метод f1() класа SuperBase')

class Base(SuperBase):
	def f2(self):
		print('Метод f2() класа Base')
		
class Child(Base):
	def f2(self):
		print('Метод f2() класа Child')
	def f3(self):
		print('Метод f3() класа Child')
		
child_object = Child()
print(Child.__mro__)