import io
s = io.StringIO('Hello, Alice!')
# s.write('Вєтаю')
# s.seek(1)
# s.write('і')
# s.seek(0, io.SEEK_END)
# s.seek(s.tell()-len('alice')-1)
# s.write('Алісо')
print(s.tell(), f'{s.getvalue()!r}')
