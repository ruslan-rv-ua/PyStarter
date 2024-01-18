def f():
    global r
    r = 'присвоєно всередині функції'
f()


'''
def f():
    r = 'присвоєно всередині функції'
    global r
f()
'''

'''
def f(r):
    global r
    r = 'присвоєно всередині функції'
f()
'''

######## nonlocal


def outer():
    r=None
    def inner():
        nonlocal r
        r='присвоєно всередині функції inner()'
    inner()
    print(r)
outer()
