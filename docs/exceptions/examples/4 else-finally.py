def div(numbers):
	try:
		result = numbers[0] / numbers[1]
	except IndexError:
		print('Треба мінімум два числа')
		return
	except ZeroDivisionError:
		print('Друге число не повинно бути 0')
		return
	except Exception as e:
		print('Піймали', e)
		return
	print(result)

'''
def div(numbers):
	try:
		result = numbers[0] / numbers[1]
	except IndexError:
		print('Треба мінімум два числа')
		return
	except ZeroDivisionError:
		print('Друге число не повинно бути 0')
		return
	finally:
		print('Функція відпрацювала')
	print(result)

def div(numbers):
	try:
		result = numbers[0] / numbers[1]
	except IndexError:
		print('Треба мінімум два числа')
	except ZeroDivisionError:
		print('Друге число не повинно бути 0')
	else:
		print(result)
	finally:
		print('Функція відпрацювала')
'''
div(1)