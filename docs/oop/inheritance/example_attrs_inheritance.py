class Base:
	def __init__(self):
		self.attr = 'Атрибут базового класа'
	def method(self):
		print('Це метод з класа Base')
		print(f'У екземпляра класа Base є атрибут {self.attr=}')
		
class Child(Base):
	def child_method(self):
		print('Це метод з класа Child')
		print(f'У екземпляра класа Child є атрибут {self.attr=}')

object_of_child = Child()
object_of_child.method()
object_of_child.child_method()
object_of_child.attr




class Base:
	def __init__(self):
		self.__attr = 'Атрибут базового класа'
	def method(self):
		print('Це метод з класа Base')
		print(f'У екземпляра класа Base є атрибут {self.__attr=}')
		
class Child(Base):
	def child_method(self):
		print('Це метод з класа Child')
		print(f'У екземпляра класа Child є атрибут {self.__attr=}')

object_of_child = Child()
object_of_child.method()
object_of_child.child_method()