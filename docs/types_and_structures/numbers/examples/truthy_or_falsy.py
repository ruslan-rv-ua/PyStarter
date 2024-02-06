def print_even(data):
	if not data: # if len(data) == 0:
		raise ValueError("The argument data cannot be empty")
	for value in data:
		if not value % 2: # if value % 2 == 0:
			print(value)
			
print_even([1,2,3,4])
print_even([])