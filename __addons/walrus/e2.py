'''
while True:
    value = input('введіть текст: ')
    if value == '':
        break
    print(f'Ви ввели: {value!r}')
print('до побачення')
'''

while (value := input('введіть текст: ')):
    print(f'Ви ввели: {value!r}')
print('до побачення')


