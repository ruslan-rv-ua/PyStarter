'''
"Усі співають пісеньку!"

'''

# ваш код тут
def get_song(repeats, words, lines):
	word = '-'.join(['ла'] * repeats)
	line = ' '.join([word] * words)
	result = '\n'.join([line] * lines)
	return result
	
print('Усі співають пісеньку:')
print(get_song(2, 4, 2))