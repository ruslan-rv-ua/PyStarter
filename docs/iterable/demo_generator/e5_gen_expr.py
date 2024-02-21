def pow2_gen():
    for n in range(11):
        if n % 2:
            yield 2**n

r = sum(pow2_gen())


g = (2**x for x in range(11) if x%2)
# g
sum(g)

for i, n in enumerate(g, start=1):
    if i > 5:
        break
    print(n)

l = [2**x for x in range(11) if x%2]

########################

