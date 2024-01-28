class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(42, 24)
p.x
# p.__dict__
# p.z = 3

############################
class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Point3D(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
    
p = Point3D(42, 24, 5)
p.__slots__
p.extra = 'oops'
p.__dict__

class Point3D(Point):
    __slots__ = ('z',)
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

p = Point3D(42, 24, 5)
p.__slots__
# p.extra = 'oops'

###########################

'''
class B1:
    __slots__ = ('b1',)
class B2:
    __slots__ = ('b2',)
class C(B1, B2):
    pass
'''



    