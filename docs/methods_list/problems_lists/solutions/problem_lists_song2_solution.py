'''
"Пісенька 2"

З пісні взяли 4 рядки тексту,
і в кожному рядку кожне слово записали "навпаки", тобто справа наліво,
причому порядок слів в кожному рядку залишився незмінним.
Написати програму яка виводить оригінальний текст у вигляді чотирьох рядків.
Підказка:
Циклом переберати рядки.
Всередині цього циклу іншим циклом перебирати слова у рядку.
'''
song_text='''вадап гінс ан гіроп
тік випілз ібос гірип
икод вижамс икод кіп
йот гірип юодов кітс'''

# ваш код тут

for line in song_text.split('\n'):
	words = line.split()
	for i in range(len(words)):
		words[i] = words[i][::-1]
	print(' '.join(words))
