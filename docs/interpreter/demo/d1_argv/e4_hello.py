from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        name = ', '.join(argv[1:])
    else:
        name = 'World'
    print(f"hello {name}!")
