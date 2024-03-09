def log_function(func):
    def wrapper(*args, **kwargs):
        args_ = [f'{arg!r}' for arg in args]
        kwargs_ = [f'{key}={value!r}' for key, value in kwargs.items()]
        print(f'➡ {func.__name__}({", ".join(args_ + kwargs_)})')
        result = func(*args, **kwargs)
        print(f'⬅ {func.__name__}: {result}')
        return result
    return wrapper

@log_function
def f(a, b):
    return a + b

f(1, b=2)