import os
from contextlib import contextmanager

@contextmanager
def cd(dir):
    old = os.getcwd()
    os.chdir(dir)
    yield
    os.chdir(old)
    
print(os.getcwd())
with cd('\\'):
    print(os.getcwd())
print(os.getcwd())

#####################
import uuid
from pathlib import Path


def temp_file(mode='w', dir=None):
    name = f"{uuid.uuid4()}.tmp"
    path = Path(os.environ['TEMP']) if dir is None else Path(dir)
    file_path = path / name
    try:
        file = open(file_path, mode)
        yield file
    finally:
        file.close()
        file.unlink()