import re

#! read this later
status_bar = 'Normal text file length : 163    lines : 13 Ln : 17    Col : 71    Pos : 164 Windows (CR LF) UTF-8 INS'
# Ln : 17    Col : 71
regexp = r'.*Ln : (\d+).*Col : (\d+).*'

m = re.search(regexp, status_bar)
l = m.group(1)
c = m.group(2)
print(l,c)

'''
додати у словник NVDA:
шаблон
.*Ln : (\d+).*Col : (\d+).*
заміна
\1:\2
коментар
для notepad++ при читанні статусного рядка оголошує лише позицію курсора у вигляді  "<номер_рядка>:<номер_стовпчика>"
Регулярний вираз  радіокнопка  позначено
'''
