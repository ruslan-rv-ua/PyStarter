try:
	1/0
except ZeroDivisionError as e:
#except Exception as e:
#except ArithmeticError as e:
	catched = e
# print(e)
print(catched)


############################

try:
	1/0
except Exception:
	print('Some exception catched')
except ZeroDivisionError:
	print('Zero division catched')

#######################

def f():
    1/0
    
try:
    1 / f()
except ZeroDivisionError:
    print('Zero division catched')

#######################

l = [1,0]
index = 2
try:
    r = 1/l[index]
except Exception as e:
    print(e)
    r = float('inf')
