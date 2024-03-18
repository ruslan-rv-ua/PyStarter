import io
with io.StringIO() as stream:
	for number in range(5):
		print(number, number**2, file=stream)
	# print(stream.getvalue())
	stream.seek(0)
    print(stream.read())
