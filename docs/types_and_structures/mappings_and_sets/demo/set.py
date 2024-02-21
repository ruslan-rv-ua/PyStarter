s = {1,2,3,1,2}

l = [4,3,2,1,2,3,4]
s = {n*n for n in l}
aaa
f = frozenset(l)
chars = set('молоко')

# iterable
r = list(chars)

########################

r = 's' in chars
################

s = {1,2,3}
s.add(1)

s.update([1,42])

s.discard(1)
s.discard(1)
# s.remove(1)

##################

s = {1,2,3}

r = s.union({2,3,4})

r = s.intersection([2,3,4])

r = s.difference({2,3,4})

r = s.symmetric_difference({2,3,4})

###############
