def outer():
    message = 'Python rocks!'
    def inner():
        print(message)
    inner()


def outer():
    message = 'Python rocks!'
    def inner():
        print(message)
    return inner

closure = outer()
closure()

##############

def outer():
    message = 'rocks!'
    def inner(who):
        print(f'{who} {message}')
    return inner

closure = outer()
closure('Python')
outer()('Rust')

######################

def outer(message):
    def inner(who):
        print(f'{who} {message}!')
    return inner

rocks = outer('rocks')
rocks('Python')
sucks = outer('sucks')
sucks('Java')
rocks('Rust')

##########################

# f(x)=ax²+bx+c
def quadratic_function(a, b, c):
    def f(x):
        return a*x*x + b*x + c
    return f
    
f1 = quadratic_function(1, 0, 0) # f(x) = x²
r=f1(5)
r=f1(9)

f2 = quadratic_function(2, 2, 2) # f(x) = 2x² + 2x + 2
r=f2(1)




