'''
"Кількість букв"

Підрахуйте скільки букв міститься у текстовому файлі "sobaka_baskerviliv.txt".
Файл у кодуванні UTF-8.
'''
f = open('sobaka_baskerviliv.txt', 'r', encoding='utf8')
text = f.read()
f.close()
letters_count = 0
for char in text:
	if char.isalpha():
		letters_count += 1
print(letters_count)