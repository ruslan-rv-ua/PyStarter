def factorial1(n):
	result = 1
	for i in range(2, n+1):
		result *= i
	return result
	
def factorial(n):
	if n == 0:
		return 1
	return n * factorial(n-1)
	
def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

r = factorial(998)
d = len(str(r))