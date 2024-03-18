# print to file
import sys
with open('temp.txt', 'w', encoding='UTF-8') as f:
	print('А я тут прінтую!', file=f)
