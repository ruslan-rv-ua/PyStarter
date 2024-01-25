def add(a, b):
	return a + b
	
def sub(a, b):
	return a - b
	
def mul(a, b):
	return a * b
	
def div(a, b):
	return a / b
	
operators = {
	'+': add,
	'-': sub,
	'*': mul,
	'/': div,
}

n1 = float(input('Enter first operand: '))
op = input('Enter operator: ')
n2 = float(input('Enter second operand: '))

res = operators[op](n1, n2)

print('Result', res)