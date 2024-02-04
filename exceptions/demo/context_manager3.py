class ErrorsSuppressor:
    def __init__(self, *args, log=True):
        self.log = log
        self.exceptions = args
        
    def __enter__(self):
        pass
        
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None and exc_type in self.exceptions:
            if self.log:
                print(f"Catched {exc_type.__name__}: {exc_value}")
            return True
        return False
            
with ErrorsSuppressor(ZeroDivisionError):
with ErrorsSuppressor(IndexError, ZeroDivisionError):
    1/0
    [][0]
    print('done')




from contextlib import suppress

with suppress(ZeroDivisionError, AttributeError):
    print('start')
    1/0
    print('end')
    

