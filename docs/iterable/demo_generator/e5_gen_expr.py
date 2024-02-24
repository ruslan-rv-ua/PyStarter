def pow2_gen():
    for n in range(11):
        if n % 2:
            yield 2**n

r = sum(pow2_gen())


g = (x*x for x in range(11) if x%2)
# g
#sum(g)

for n in g:
    if n > 30:
        break
    print(n)

l = [x*x for x in range(11) if x%2]

########################

