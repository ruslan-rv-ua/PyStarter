def f(x):
    try:
        return 1/x
    except ZeroDivisionError:
        pass
    finally:
        print('ZeroDivisionError detected!')
        
r = f(1)