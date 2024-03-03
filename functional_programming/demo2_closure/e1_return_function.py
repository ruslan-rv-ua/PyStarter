def outer():
    def inner():
        message = 'Hello!'
        print(message)
    # print(inner)
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
