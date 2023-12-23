len = 'global'
def outer():
    len = 'enclosing'
    def inner():
        len = 'local'
        print(len)
    inner()

outer()

