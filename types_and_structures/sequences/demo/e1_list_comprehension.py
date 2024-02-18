r=[]
for n in range(5):
    r.append(n)
    
l=[n for n in range(5)]

###########################

r=[]
for n in range(5):
    if n%2:
        r.append(n)
    
l=[n for n in range(5) if n%2]

###########################

r=[]
for n in range(5):
    if n%2:
        r.append(n*n)
    
l=[n*n for n in range(5) if n%2]

###########################

text = 'Скільки буде 2 помножити на 2?'
# порахувати суму усіх цифр у тексті
s = sum([int(char) for char in text     ])

###########################

def make_matrix(rows, cols):
    return [[0]*cols for _ in range(rows)]
    
m = make_matrix(2,2)
m[0][0] = 42

#####################################

text = 'PyStarter is amazing'
# отримати рядок з перших букв слів у верхньому регістрі
s = ''.join([word[0].upper() for word in text.split()])

#####################################

# табличка множення
t = [[a*b for a in range(1, 11)] for b in range(1, 11)]
# st = '\n'.join([''.join([f'{num:4d}' for num in row]) for row in t])
print('\n'.join([''.join([f'{num:4d}' for num in row]) for row in t]))


#####################################


text = "У процесі вивчення нових статистичних методів ми аналізували дані з чотирьох експериментів. Середні значення цих експериментів становили 3.6, 7.2, 5.1, і 9.8 відповідно."
numbers = [float(x) for x in text.replace(",", "").split() if x.replace(".", "", 1).isdigit()]


#####################################
