class WashingMachine:
	def start(self):
		print('Starting wash your cloths')
	   
class Computer:
	def start(self):
		print('Windows is starting')
		
def start(obj):
	obj.start()

for some_device in WashingMachine(), Computer():
	start(some_device)
	some_device.start()

class Duck:
	def quack(self):
		print('Кря!')

class Person:
	def __init__(self, name):
		self._name = name
	def quack(self):
		print('Людина імітує крякання: "Кря!"')

#for any in Duck(), Person('John'):
#	any.quack()

	
class MyInt(int):
	def __len__(self):
		return len(str(self))
	def __add__(self, other):
		return MyInt(str(self) + str(other))
		
n1 = MyInt(12)
n2 = MyInt('3')
r = n1+n2