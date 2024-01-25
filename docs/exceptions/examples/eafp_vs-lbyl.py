'''
# LBYL
while True:
	s = input('Enter first integer: ')
	if s.strip().isdigit():
		n1 = int(s)
		break
	else:
		print('Not integer number!')
while True:
	s = input('Enter second integer: ')
	if s.strip().isdigit():
		n2 = int(s)
		if n2 != 0:
			break
		else:
			print('Can not divide by zero!')
	else:
		print('Not integer number!')
print(n1/n2)			
'''

	
	
	
	
	
# EAFP
while True:
	try:
		n1 = int(input('Enter first integer: '))
		break
	except ValueError:
		print('Not number!')
	
while True:
	try:
		n2 = int(input('Enter second integer: '))
		print(n1/n2)
		break
	except ValueError:
		print('Not number!')
	except ZeroDivisionError:
		print('Can not divide by zero!')
		

	