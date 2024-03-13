# read(), write()

import sys
i = sys.stdin
o = sys.stdout
e = sys.stderr

# a = i.read()
o.write('Привіт!')

###################

from time import sleep

print('hello ', end='', flush=True)
sleep(5)
print('world')

##################

# low level
import os
print(os.open)
# file descriptor

#######################

# open - в модулі io
import io
r = io.open is open
