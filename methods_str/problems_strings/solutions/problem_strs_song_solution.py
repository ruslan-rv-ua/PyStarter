'''
"Пісенька"

З пісні взяли 4 рядки тексту,
і кожен рядок записали справа наліво.
Написати програму яка виводить оригінальний текст у вигляді чотирьох рядків.
'''
song_text = """dneirf ysae na deen I
dnel ot rae na htiw ,od I
eohs siht tif uoy kniht t'nod I
eulc a evah uoy t'now ,od I"""
# далі ваш код
for line in song_text.split('\n'):
	print(line[::-1])