'''
"Дай 7!"

Реалізувати функцію, яка приймає список чисел і перевіряє, 
чи можна скласти будь-які три різних числа з цього списка так, щоб отримати число 7.
Якщо числе меньше 3, повернути False.
'''
def can7(numbers):
	# ваш код тут
	for i1 in range(len(numbers) - 2):
		for i2 in range(i1+1, len(numbers) - 1):
			for i3 in range(i2+1, len(numbers)):
				if numbers[i1] + numbers[i2] + numbers[i3] == 7:
					return True
	return False
	
# тести	
assert can7([2, 4, 3, 8, 9, 1]) == True
assert can7([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True
assert can7([0, 0, 0, 2, 3]) == False
assert can7([4, 3]) == False
