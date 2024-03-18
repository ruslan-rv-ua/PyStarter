# read(), write()

import sys
i = sys.stdin
o = sys.stdout
e = sys.stderr

# a = i.read()
o.write('Привіт!')
# o.flush()
###################

from time import sleep

print('hello ', end='', flush=False)
sleep(3)
print('world')

##################

# low level
import os
# print(os.open)
# file descriptor

#######################

# open - в модулі io
import io
r = io.open is open
