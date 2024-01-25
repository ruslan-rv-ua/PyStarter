try:
	1/0
except Exception:
	print('Some exception catched')
except ZeroDivisionError:
	print('Zero division catched')
