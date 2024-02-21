class C:
    def __format__(self, format_spec):
        return f'{format_spec=}'
		
o=C()
print(f'{o:%h:%m}')

b='Привіт'.encode(encoding='utf8')
s=b.decode(encoding='utf8')


s='\N{GRINNING FACE}'
