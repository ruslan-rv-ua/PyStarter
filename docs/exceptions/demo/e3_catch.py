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

l = [2,1,0]
index = 2
try:
    1/l[index]
except Exception:
    print("Сталось ділення на нуль!")

    
l = [2,1,0]
index = 2
try:
    1/l[index]
except Exception:
    print("Сталось ділення на нуль!")
