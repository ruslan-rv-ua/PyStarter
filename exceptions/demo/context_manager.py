'''
file = open('some_file.txt', 'w')
try:
    file.write(...)
finally:
    file.close()

with open('some_file.txt', 'w') as file:
    file.write(...)
'''
    
# __enter__(self)

# __exit__(self, exception_class, exception_obj, exception_traceback)

import os

class cd:
    def __init__(self, path):
        self.path = path
    def __enter__(self):
        self.old_path = os.getcwd()
        os.chdir(self.path)
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        os.chdir(self.old_path)
    def __repr__(self):
        return f"cd {self.path}"
    @staticmethod
    def cwd():
        return os.getcwd()

print(os.getcwd())
with cd("\\") as dir1:
    print(os.getcwd())
print(os.getcwd())

################################

import time

class MeasureTime:
    def __enter__(self):
        self.start_time = time.time()
        return self  # Повертаємо себе, якщо є необхідність працювати з деяким об'єктом у блоку with

    def __exit__(self, exc_type, exc_value, traceback):
        elapsed_time = time.time() - self.start_time
        print(f"Час виконання: {elapsed_time} секунд")

with MeasureTime():
    for _ in range(1000000):
        pass


