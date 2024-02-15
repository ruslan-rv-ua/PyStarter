'''
__add__
__radd__
__iadd__
__neg__
__abs__
'''

# __int__()
from datetime import datetime
class MyDateTime(datetime):
    def __int__(self):
        return int(self.timestamp())
d = MyDateTime.now()
r = int(d)


from numbers import *

# __float__()
float('-inf')
float('nan')
from math import nan, isnan
