> ***Множина*** – невпорядкована колекція об'єктів, що хешуються, які не повторюються.

Типове використання множин — перевірка певного елемента на входження в множину та видалення повторів елементів і виконання таких операцій, як об'єднання, пересічення, різниця і симетрична різниця. 

В множинах немає поняття позиції елемента. Відповідно, вони не підтримують індексацію і зрізання. 

s = {1, 2, 3, 2, 3, 3}

s = {x*x for x in range(10) if x%2}

s = set()
fs = frozenset([4, 1, 4, 3, 8])
l = set('abrakadabra')

len(l)
4 in fs


s.add(4) 

s.update({2, 4, 6})
s |= {11}

s.update([10, 20]) 

s.discard(10) 

s.remove(20)
s.remove(21)

s.pop()
s.clear() 
s.pop()


js = {'Дарія', 'Наталія', 'Володимир', 'Андрій'}
py = {'Дарія', 'Володимир', 'Андрій', 'Руслан'}
def p(s):
	print(' '.join(s))


об’єднання повертає множину, що складається з елементів, які належать хоча б одній з двох множин: 
p(js.union(py))
p(js|py)
	
перетин повертає множину, що складається з елементів, які належать одночасно двом множинам: 
p(js.intersection(py))
p(js&py)


різниця повертає множину з тих елементів, які не належать переданій множині: 
p(js.difference(py))
p(py.difference(js))
p(py-js)

симетрична різниця повертає множину з тих елементів, які належать рівно одній з множин: 
p(js.symmetric_difference(py))
p(js^py)


