import json

'''
data = [
    {'name': 'Петро','age': 30,},
    {'name': "Мар'яна",'age': 29},
]

with open('data.json', 'w', encoding="UTF-8") as file:
    json.dump(data, file, indent=2, ensure_ascii=False)
'''
# Десериализация
with open('data.json', encoding='UTF-8') as file:
    data = json.load(file)
print(data)
