
x = []
def f():
	x = [1, 2, 3]
f()

# global
# x = 'global'
def function():
    global x
    x = 'global assigned inside function'
    print (x)
	
def function():
    x = 'global assigned inside function'
    global x
    print (x)


function()


# nonlocal

def outer():
    x = "x assigned inside outer"
    def inner():
        x = "x assigned inside inner"
        print("inner():", x)
    inner()
    print("outer():", x)

outer()


def outer():
    x = "x assigned inside outer"
    def inner():
        nonlocal x
        x = "x assigned inside inner"
        print("inner():", x)
    inner()
    print("outer():", x)

outer()




def outer():
    x = "x assigned inside outer"
    def inner():
        nonlocal x, unknown
        x = "x assigned inside inner"
        print("inner():", x)
    inner()
    print("outer():", x)
