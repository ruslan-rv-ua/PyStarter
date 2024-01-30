# compile time exceptions
# runtime exceptions

for e in BaseException.__subclasses__():
	print(e.__name__)

for e in Exception.__subclasses__():
	print(e.__name__)

e = ZeroDivisionError()
e = ZeroDivisionError('Погано ти ділиш!')
e = ZeroDivisionError('Погано ти ділиш!', 'extra_data')
e.args

r = isinstance(e, ArithmeticError)
r = isinstance(e, Exception)
# try mro()
raise e

