# print to file
import sys
with open('f02.txt', 'w', encoding='UTF-8') as f:
	print('А я тут прінтую!', file=f)
