'''
Напишіть програму яка виконує наступне:
1. Дано два рядки:
   text1 = "Python3.10Programming"
   text2 = "SAMPLE"
   
2. Створити нові змінні, використовуючи ТІЛЬКИ індексацію та зрізи:
   - first: перші 6 символів з text1 у зворотному порядку
   - second: символи з text2 з парними індексами
   - third: останні 4 символи з text1
   - result: об'єднати first, second і third
'''
text1 = "Python3.10Programming"
text2 = "SAMPLE"
# ваш код починається з наступного рядка

first = text1[5::-1]
second = text2[::2]
third = text1[-4:]
result = first + second + third

# не міняйте наступний код
assert first == "nohtyP"
assert second == "SML"
assert third == "ming"
assert result == "nohtyPSMLming"
