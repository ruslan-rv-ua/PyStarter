from os import chdir, getcwd
from contextlib import contextmanager

@contextmanager
def cd(path):
    old_dir = getcwd()
    chdir(path)
    try:
        yield
    finally:
        chdir(old_dir)


print(getcwd())
with cd("\\"):
    print(getcwd())
print(getcwd())

