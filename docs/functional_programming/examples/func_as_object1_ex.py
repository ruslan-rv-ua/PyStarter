def f(x):
    return x + 3
 
def g(function, x):
    return function(x) * function(x)
 
print(g(f, 7))






def to_lower(string):
	return string.lower()

l = ['John', 'jam', 'Jane', 'job']
	
sorted_list = sorted(l, key=to_lower)
	
for i in sorted_list:
	print(i)