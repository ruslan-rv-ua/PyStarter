def product_info(name, color, price):
    print('Назва:', name)
    print('Колір:', color)
    print('Ціна:', price)
    
product_info('Олівець', 'червоний', 2)
product_info(2, 'червоний', 'Олівець')
product_info(price=2, color='червоний', name='Олівець')
product_info('Олівець', price=2, color='червоний')
# product_info(price=2, 'Олівець', color='червоний')

def product_info(name, color='зелений', price=7):
    print('Товар:', name)
    print('Колір:', color)
    print('Ціна:', price)

product_info('Зошит')
product_info('Зошит', price=5)

def modify_list(lst=[]):
    lst.append(42)
    return lst

l=modify_list()
l=modify_list([1])
l=modify_list()

def modify_list(lst=None):
    if lst is None:
        lst = []
    lst.append(42)
    return lst

##########

def f(x, /):
    print(x)
    
# f(x=2)
# sin(x, /)

def f(*, x):
    print(x)

# f(2)


def sorted(iterable, /, *, key=None, reverse=False):
def dump(
        obj, *, skipkeys, ensure_ascii, check_circular, allow_nan, cls, indent, separators, default, sort_keys
    ):
    pass
    
###############

def f(*args):
    for a in args:
        print(a)
        
f(1)
f(1, 'hello', [1,2,3])
f()

def f(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

f(name='Alice',  age=25)
f()


