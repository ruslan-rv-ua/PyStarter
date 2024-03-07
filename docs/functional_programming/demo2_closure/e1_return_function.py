def outer():
    def inner():
        message = 'Hello!'
        print(message)
    inner()
outer()

def outer():
    def inner():
        message = 'Hello!'
        print(message)
    return inner
f = outer()

def outer():
    def inner(message):
        print(message)
    return inner
f = outer()
f('Python')