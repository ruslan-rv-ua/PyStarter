##### local

def f():
    x=42
f()
# print(x)

#### global
x=42
def f():
    print(x)
f()

##### builtin
def f():
    print(print)
f()

##### enclosing
list = 'це глобальна змінна'
def outer():
    list = 'це локальна змінна функції outer()'
    def inner():
        list = 'це локальна змінна функції inner()'
        print(f'{list=}')
    inner()
outer()

