l = [1, 2, 3]
l.append(4)
l.append([4, 5])
l.append('text')

l = [1, 2, 3]
l.extend('text')
l.extend([4, 5])

l = [1, 2, 3]
l.insert(0, 0)
l.insert(-1, 2.5)
l.insert(1000, 1000)
l.insert(-1000, -1000)

l = [1, 2, 3]
l.remove(1)
# l.remove(11)

l = [1, 2, 3]
r = l.pop(0)
r = l.pop()
# r = l.pop(11)

l = [1, 2, 3]
r = l.index(3)
# r = l.index(11)

l = [1, 2, 3]
r = l.count(1)
r = l.count(11)

l = [1, 2, 3]
r = l.sort(reverse=True)

l = [1, 2, 3]
l2 = l
l2.clear()

l.reverse()

# stack
stack.push(x)
r = stack.pop()
v = stack.peek()
