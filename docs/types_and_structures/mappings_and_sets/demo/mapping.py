d = {n:str(n)*2 for n in range(1, 6) if n%2}


people = ['John', 'Jane', 'Mary', 'Bob', 'Alice']
d = {key:value for key, value in enumerate(sorted(people), start=1)}


d = dict(key1=11, key2=22)

d = dict([(1,11), [2,22]])
d = dict.fromkeys('abc', 42)

