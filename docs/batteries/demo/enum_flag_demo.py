import enum

class Permission(enum.IntFlag):
    R = enum.auto()
    W = enum.auto()
    X = enum.auto()
    
    def __str__(self):
        result = ''
        for flag in Permission:
            result += flag.name.lower() if flag & self else '-'
        return result

rw = Permission.R | Permission.W
a=str(rw)
x = Permission.X

