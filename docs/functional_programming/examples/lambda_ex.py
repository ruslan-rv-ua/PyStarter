def add(x, y):
	return x + y
	
add = lambda x, y: x + y

(lambda x, y: x + y)(5, 7)

hello = lambda name, time='morning': 'Good ' + time + ', ' + name
hello('Jane')
hello('Jane', 'afternoon')

func = lambda *args: args
func(1, 2, 3, 4)

mymin = lambda x, y: x if x < y else y
mymin(1,3)

---

authors = [
	"Edgar Allan Poe",
	"Arthur Conan Doyle",
	"Agatha Christie",
	"John Dickson Carr"
]

authors = sorted(authors, key=lambda a: a.split()[-1])	
print('\n'.join(authors))

---

functions = [
	lambda x: x**2,
	lambda x: x**3,
	lambda x: x**4,
]

d = {
	'add': lambda x, y: x + y,
	'mul': lambda x, y: x * y
}

d['add'](5, 5)
d['mul'](5, 5)