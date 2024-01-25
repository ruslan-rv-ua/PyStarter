def calc(string):
	operators = {
		'+': lambda a, b: a + b,
		'-': lambda a, b: a - b,
		# '*': lambda a, b: a * b,
	}
	for op in operators:
		if op in string:
			left, _, right = string.partition(op)
			return operators[op](calc(left), calc(right))
	return int(string)
			
expr = '1+1-2+100-50'
# expr = '2+2-3+5-10'
res = calc(expr)
assert res == eval(expr)
print(res)
