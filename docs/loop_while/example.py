number = 0
while number <= 5:
	print(number)
	number = number + 1
	
def print_nums(from_inclusive, to_exclusive):
	number = from_inclusive
	while number < to_exclusive:
		if number % 2 == 0:
			print(number)
		number = number + 1

print_nums(0, 5)

def sum_of_range(from_inclusive, to_exclusive):
	sum = 0
	number = from_inclusive
	while number < to_exclusive:
		sum += number
		number += 1
	return sum
	
print(sum_of_range(0, 4))

def multiply_string(string, times):
	result = ''
	while times > 0:
		result += string
		times -= 1
	return result
	
print(multiply_string('a', 3))

def print_symbols(string):
	i = 0
	while i < len(string):
		print(string[i])
		i += 1
		
print_symbols('')