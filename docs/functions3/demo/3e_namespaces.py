# builtin
import builtins

# global
# print(list(globals().keys()))
print(globals().keys())
# print([name for name in globals() if not name.startswith('__')])

var=42
print([name for name in globals() if not name.startswith('__')])

globals()['var'] = 42
# from math import *
print([name for name in globals() if not name.startswith('__')])

##### local

def f(parameter):
    locals()['local_var']=42
    # local_var = 42
    print([name for name in locals() if not name.startswith('__')])
    print(local_var)
f(42)

print(locals())

