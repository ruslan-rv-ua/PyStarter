'''
"Премія"

Одна фірма виплачує щомісячну премію в залежності від того, 
скільки працівник присвятив часу роботі у даній фірмі.
Принцип нарахування наступний:
- меньше 2 років — премія не нараховується
- 2 роки і більше — 2% від ставки
- 5 років і більше — 4% від ставки
- 10 років і більше — 10% від ставки
Напишіть програму яка виконує наступне:
1. Просить користувача ввести розмір ставки і стаж працівника
2. Виводить нараховану зарплатню — ставка плюс премія
'''
# ваш код починається тут

# отримуємо вхідні дані
salary = float(input('Введіть зарплату: '))
exp = int(input('Введіть стаж роботи: '))

# визначаємо розмір премії
if exp >= 10:
	bonus_percent = 10
elif exp >= 5:
	bonus_percent = 4
elif exp >= 2:
	bonus_percent = 2
else:
	bonus_percent = 0
	
# обчислюємо розмір зарплати
total = salary * (1 + bonus_percent * .01)

# виводимо результат
print('Зарплата:', total)