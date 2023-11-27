'''
"Нейтралізація"

Реалізуйте функцію neutralize().
Функція приймає два символьних рядки однакової довжини які складаються зі знаків «+» і «-».
Функція повертає символьний рядок — результат взаємодії параметрів.

Передані рядки взаємодіють наступним чином:
- плюс і плюс дають плюс
- мінус і мінус дають мінус
- плюс і мінус нейтралізують один одного і в результаті дають 0.
Приклад.
neutralize("+-+", "+--") == "+-0"
Порівнюємо перші символи двох рядків, потім наступні два символи і так далі:
"+" і "+" дають "+".
"-" і "-" дають "-".
"+" и "-" дають "0".
'''
def neutralize(s1, s2):
	# ваш код тут
	result = ''
	for i in range(len(s1)):
		if s1[i] != s2[i]:
			result += '0'
		else:
			result += s1[i]
	return result
	
def neutralize(s1, s2):
	return ''.join('0' if a != b else a for a, b in zip(s1, s2))
	
assert neutralize("+-+", "+--") == "+-0"
assert neutralize("--++--", "++--++") == "000000"
assert neutralize("-++-", "-+-+") == "-+00"
assert neutralize("-+-+-+", "-+-+-+") == "-+-+-+"
assert neutralize("--++--", "++--++") == "000000"
assert neutralize("-+-+-+", "-+-+-+") == "-+-+-+"
assert neutralize("-++-", "-+-+") == "-+00"
