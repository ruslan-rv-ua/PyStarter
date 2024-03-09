def run_once(func):
    called = False
    def wrapper(*args, **kwargs):
        nonlocal called
        if not called:
            called = True
            return func(*args, **kwargs)
        raise RuntimeError("Вже викликали цю функцію")
    return wrapper
	
@run_once
def f():
	print('функція запущена')
     
# f()
# f()

# print = run_once(print)
# print(1)
# print(2)

#######################

def run_once(func):
    def wrapper(*args, **kwargs):
        if not wrapper.called:
            wrapper.called = True
            return func(*args, **kwargs)
        raise RuntimeError("Вже викликали цю функцію")
    wrapper.called = False
    return wrapper
	
@run_once
def f():
	print('функція запущена')

# f.called
# f()
# f.called