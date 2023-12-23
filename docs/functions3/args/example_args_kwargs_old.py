def adder(a, b):
	return a + b

s = adder(3, 5)
# print(s)

# ---

def adder(*args):
    res = 0
    for num in args:
        res += num
    return res
	
# ---

def my_min(first, *args):
	res = first
	for arg in args:
		if arg < res:
			res = arg
	return res
	


def all_i_got(**kwargs):
    for key in kwargs:
        print(f'{key} is {kwargs[key]}')
		
# all_i_got(item='Aplle iPhone 5s', price=99.99, colors=['black','silver'])


#---

def tail(sequence, *, length=1):
    print(sequence[-length:])

# tail('Hello, World', 6)
tail('Hello, World', length=6)


	

# усі разом

