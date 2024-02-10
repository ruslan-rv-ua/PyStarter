from contextlib import suppress, redirect_stdout

with suppress(ZeroDivisionError, AttributeError):
    1/0
    print('done')
    



class NoErrors:
    def __init__(self, *args, log=True):
        self.exceptions = args
        self.log = log
        
        
    def __enter__(self):
        pass
        
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None and exc_type in self.exceptions:
            if self.log:
                print(f"Catched {exc_type.__name__}: {exc_value}")
            return True
        return False
            
with NoErrors(IndexError, ZeroDivisionError):
# with NoErrors(ZeroDivisionError):
    1/0
    [][0]
    print('done')




