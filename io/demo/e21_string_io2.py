import io
with io.StringIO() as stream:
	for number in range(5):
		print(number, file=stream)
	print(stream.getvalue())
		