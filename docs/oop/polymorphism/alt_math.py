from numbers import Integral

class AltInt(int):
    def __len__(self):
        return len(str(self))
    def __add__(self, other):
        # if not isinstance(other, (AltInt, int)):
        if not isinstance(other, Integral):
            raise TypeError(f"unsupported operand type(s) for +: '{self.__class__.__name__}' and '{other.__class__.__name__}'")
        return AltInt(str(self) + str(other))
        
n1 = AltInt(2)
n2 = AltInt('2')
r = n1+n2
r = AltInt('11') + 22
# r = AltInt('11') + '22'
# r = 11 + AltInt(22)
