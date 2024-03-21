l = [1,2,3,4,5]

# куби чисел, якщо цей куб меньше 20

def cube(x):
    return x*x*x

l2 = [cube(n) for n in l if cube(n) < 20]
l2 = [c for n in l if (c:=cube(n)) < 20]