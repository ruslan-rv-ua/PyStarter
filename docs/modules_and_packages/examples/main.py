import sys
# print(sys.path)

def f():
	pass
	
def test():
	assert f() == None
	
if __name__ == '__main__':
	test()

from usefull import long_function_name as lfn, func

Оператор from...import можна концептуально представити наступним способом:

import usefull
lfn = usefull.long_function_name
func = usefull.func
del usefull
	
# from m1 import *	
# from m2 import *
# from m2 import a, b
import m2
