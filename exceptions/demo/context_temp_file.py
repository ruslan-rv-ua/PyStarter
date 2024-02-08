import uuid
from pathlib import Path
import os

class temp_file():
    def __init__(self, mode='w', dir=None):
        self._mode = mode
        name = f"{uuid.uuid4()}.tmp"
        path = self._get_temp_path() if dir is None else Path(dir)
        self._file_path = path / name
    @staticmethod
    def _get_temp_path():
        try:
            path = Path(os.environ['TEMP'])
        except KeyError:
            path = Path()
        if not path.exists():
            path = Path()
        print(f"{path=}")
        return path
    def open(self):
        self._file = open(self._file_path, self._mode)
        return self._file
    def close(self):
        self._file.close()
        self._file_path.unlink()
    def __enter__(self):
        return self.open()
    def __exit__(self, exc_class, exc_obj, traceback):
        self.close()

with temp_file(dir='U:\\1') as f:
    f.write('hello')
    input('press enter')

