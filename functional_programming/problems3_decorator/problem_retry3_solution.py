'''Створити декоратор `retry`.
Якщо при виконанні декорованої функції виникає помилка, декорована функція виконується ще раз.
Усього 3 спроби.
Спробуйте виконати цю ж задачу в об'єктно-орієнтованому стилі.
'''

from functools import wraps

def retry(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for _ in range(3):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                exc = e
                print(f'Error: {exc}')
        raise exc
    return wrapper

@retry
def divide(a, b):
    return a / b

print(divide(10, 0))

class retry:
    def __init__(self, func):
        self._func = func
        self._count = 0

    def __call__(self, *args, **kwargs):
        for _ in range(3):
            try:
                return self._func(*args, **kwargs)
            except Exception as e:
                exc = e
                print(f'Error: {exc}')
        raise exc

@retry
def divide(a, b):
    return a / b

print(divide(10, 0))