class_attr = 'global'
class A:
    def f(self):
        print(self.class_attr)

c=A()
c.f()