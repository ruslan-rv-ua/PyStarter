import io
s = io.StringIO('Hello, Alice!')
print(f'{s.getvalue()!r}\n', s.tell())

s.write('Вєтаю')
s.seek(1)
s.write('і')
s.seek(0, io.SEEK_END)
s.seek(s.tell()-len('Alice!'))
s.write('Алісо')

print(f'{s.getvalue()!r}\n', s.tell())
