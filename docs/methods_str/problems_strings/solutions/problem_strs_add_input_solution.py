'''
Напишіть програму яка виконує наступне:
1. Просить користувача ввести два цілих числа розділивши їх пробілом
2. Виводить суму цих чисел

Пам'ятайте:
1. отримали вхідні дані
2. обчислили результат
3. вивели результат
'''
answer = input('Введіть два числа розділивши їх пробілом: ')
parsed = answer.split()
result = int(parsed[0]) + int(parsed[1])
print(result)