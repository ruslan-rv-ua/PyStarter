def run_once(func):
    called = False
    def wrapper(*args, **kwargs):
        nonlocal called
        if not called:
            called = True
            return func(*args, **kwargs)
        else:
            raise RuntimeError("Вже викликали цю функцію")
    return wrapper
	
@run_once
def f():
	print('функція запущена')
     
f()
# f()
