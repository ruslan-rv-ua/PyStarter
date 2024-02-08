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

print(os.getcwd())
with cd("\\") as dir1:
    print(os.getcwd())
print(os.getcwd())

################################
