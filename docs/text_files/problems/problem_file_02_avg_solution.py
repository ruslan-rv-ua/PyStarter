'''
"Числа"

У текстовому файлі "numbers.txt" записані натуральні числа, по одному у кожному рядку.
Але деякі рядки у файлі можуть бути пустими.
Вирахуйте середнє арифметичне записаних у файлі чисел.
Файл у кодуванні UTF-8.
'''

total = 0
count = 0
f = open('numbers.txt', 'r', encoding='utf8')
for line in f:
	line = line.strip()
	if line:
		total += int(line)
		count += 1
f.close()
print(total/count)