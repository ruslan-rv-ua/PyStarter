import uuid
from pathlib import Path

class temp_file():
    def __init__(self, mode='w', dir=None):
        self._mode = mode
        name = f"{uuid.uuid4()}.tmp"
        path = Path() if dir is None else Path(dir)
        self._file_path = path / name
    def __enter__(self):
        self._file = open(self._file_path, self._mode)
        return self._file
    def __exit__(self, exc_class, exc_obj, traceback):
        self._file.close()
        self._file_path.unlink()

with temp_file() as f:
    f.write('hello')
    f.flush()
    input('press enter')














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

