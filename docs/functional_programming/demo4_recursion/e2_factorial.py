def factorial1(n):
	res = 1
	for multiplier in range(2, n+1):
		res *= multiplier
	return res
	
def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

r = factorial(998)
