from sys import argv

print(argv)

if __name__ == "__main__":
	if len(argv) > 1:
		name = argv[1]
	else:
		name = 'World'
	print(f"hello, {name}!")
