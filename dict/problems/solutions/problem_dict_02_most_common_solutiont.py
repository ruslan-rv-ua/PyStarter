# ваш код з наступного рядка, умова задачі далі
def most_common_char(string):
	counter = {}
	for char in string:
		counter[char] = counter.get(char, 0) + 1
	max_count = max(counter.values())
	for char in string:
		if counter[char] == max_count:
			return char


'''
"Найчастіший символ"

Реалізуйте функцію most_common_char(string).
Функція приймає непустий символьний рядок string.
Функція визначає і повертає символ, який зустрічається у символьному рядку string найбільшу кількість раз.
Якщо декілька символів зустрічаються однакову кількість раз, повернути перший з початку символьного рядка string.
'''
# не міняйте наступний код, це тести
assert most_common_char('1') == '1'
assert most_common_char('1  2') == ' '
assert most_common_char('12') == '1'
assert most_common_char('122') == '2'
assert most_common_char('1223') == '2'
assert most_common_char('12233') == '2'
assert most_common_char('122333') == '3'
assert most_common_char('абабагаламага') == 'а'
assert most_common_char('У бобра добра багато') == 'б'