def decorator(func):
    def wrapper():
        func()
    return wrapper
    
@decorator
def simple_function():
    """Docstring for `simple_function()`"""

simple_function.__doc__
simple_function.__name__

def decorator(func):
    def wrapper():
        func()
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper
    
@decorator
def simple_function():
    """Docstring for `simple_function()`"""

##########################################

from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper():
        func()
    return wrapper
    
@decorator
def simple_function():
    """Docstring for `simple_function()`"""

simple_function.__doc__
simple_function.__name__
