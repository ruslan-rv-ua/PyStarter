for e in BaseException.__subclasses__():
	print(e.__name__)


#for e in Exception.__subclasses__():
#	print(e.__name__)


class MyAppException(Exception):
	pass
	
class ParserError(MyAppException):
	pass
	
# raise ParserError
#raise ParserError('невалідні вхідні дані')