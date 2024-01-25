'''
def a(param):
	return b(param)
	
def b(param):
	return c(param)
	
def c(param):
	return 1 / param

a(0)

n = 0

def f():
	global n
	n += 1
	f()
	
# f()


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
	
'''
	
def fib(n):
	if n == 1 or n == 2:
		return 1
	else:
		return fib(n-1) + fib(n-2)

		
def fib(n):
	if n == 1 or n == 2:
		return 1
	if n in fib.saved:
		return fib.saved[n]
	fib.saved[n] = fib(n-1) + fib(n-2)
	return fib.saved[n]
fib.saved = {}
	
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(1500)
for i in range(1000, 1001):
	print(i, fib(i))
	
