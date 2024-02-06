'''
try:
    1/0
except ZeroDivisionError:
    a+=1
'''

try:
    1/0
except ZeroDivisionError as e:
    raise ValueError from e # from None

