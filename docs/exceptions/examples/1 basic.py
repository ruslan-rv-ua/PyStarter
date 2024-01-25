try:
	1/0
except ZeroDivisionError as e:
	print('Zero division detected!', e)
print('done!')
