def f(string):
    if string[0] == '-':
        string = string[1:]
    if string.replace('.', '', 1).isdigit():
        return True
    return False
    
r = f('-42.3')

def f(string):
	try:
		float(string)
		return True
	except ValueError:
		return False

r = f('-42.3')

#############################
      
from pathlib import Path

file = Path.home() / 'some_file.txt'
if file.exists():
	text = file.read_text()
else:
	print('File does not exist')
      

try:
	text = file.read_text()
except FileNotFoundError:
	print('File does not exist')
	
