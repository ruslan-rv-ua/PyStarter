from numbers import *

# __int__()

# __float__()
float('-inf')
float('-nan')
from math import nan, isnan

'''
__add__
__radd__
__iadd__
__neg__
__abs__
'''

from datetime import datetime
class MyDateTime(datetime):
    def __int__(self):
        return int(self.timestamp())

d = MyDateTime.now()