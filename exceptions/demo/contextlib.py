import os
from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove('some_file.txt')
    
####################

from contextlib import redirect_stdout

with open('help.txt', 'w') as f:
    with redirect_stdout(f):
        help(list)
        
with open('help.txt', 'w') as f:
    with redirect_stdout(f):
        print('PyStarter')
    

###########
# contextlib.chdir

from contextlib import chdir

print(os.getcwd())
with chdir('\\'):
    print(os.getcwd())
print(os.getcwd())

