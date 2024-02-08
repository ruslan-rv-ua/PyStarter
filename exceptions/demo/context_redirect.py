from contextlib import redirect_stdout

with open('help.txt', 'w') as f, redirect_stdout(f):
    print('PyStarter!')
