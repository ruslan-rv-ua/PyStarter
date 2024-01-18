"""
Уважно прочитайте наступний початковий код. Звертайте увагу на вкладеність блоків.
Дослідіть і поясніть для себе як він працює.
"""
def outer():
    print('start "outer()"')
    def inner():
        print('start "inner()"')
        print('finish "inner()"')
    inner()
    print('finish "outer()"')
    
outer()
