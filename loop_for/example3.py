for char in 'Привіт':
	print(char)

numbers = [1, 2, 3, 4, 5, 6, 7]
for number in numbers:
	print(number)

total = 0
for number in numbers:
	if number % 2:
		total += number
print(total)
		
matrix = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9],
]
for row in matrix:
	line = ''
	for number in row:
		line += str(number) + ' '
	print(s)

	
r = range(1, 11)
r = range(11)
r = range(1, 11, 2)

numbers = list(range(11))
for i in range(len(numbers)):
	numbers[i] *= 2

numbers = list(range(-100, 101))
for number in numbers:
	if number:
		continue
	
numbers = list(range(10, 100))
for index in range(len(numbers)):
	if numbers[index] == 7:
		break
else:
	index = -1
print('Індекс елемента зі значенням 7:', index)


def find_seven(numbers):
	for i in range(len(numbers)):
		if numbers[i] == 7:
			return i
	return -1
	
numbers = list(range(10, 100))
print('Індекс елемента зі значенням 7:', find_seven(numbers))