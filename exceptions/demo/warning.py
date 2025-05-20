from warnings import warn

class IncorrectNameWarning(UserWarning):
    pass
    
class Person:
    def __init__(self, name):
        if len(name.split()) > 3:
            warn(
                f'Name maybe incorrect: {name}',
                # IncorrectNameWarning,
                # stacklevel=2
            )
        self.name = name
        
        
p = Person('Остап Сулейман Берта Марія Бендер')

#############################

from warnings import warn

def f():
    warn(f"Function 'f()' deprecated", DeprecationWarning, stacklevel=2)
    
for _ in range(5):
    f()
