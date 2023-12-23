from math import sin
def sin(x, /):
	
from json import dumps
def dumps(obj, *, skipkeys, ensure_ascii, check_circular, allow_nan, cls, ...
dumps(some_object, indent=2, sort_keys=False)

def f(pos_only, /, standard, *, kwd_only):
	print(pos_only, standard, kwd_only)
f(1, 2, 3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: combined_example() takes 2 positional arguments but 3 were given

f(1, 2, kwd_only=3)
1 2 3

f(1, standard=2, kwd_only=3)
1 2 3

f(pos_only=1, standard=2, kwd_only=3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: combined_example() got an unexpected keyword argument 'pos_only'

