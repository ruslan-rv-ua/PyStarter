def counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc
    
c1 = counter()
c2 = counter()
c1()
c1()
c1()
c2()
c2()
