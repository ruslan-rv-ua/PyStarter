import json

data = [
    {'name': 'Петро','age': 30,},
    {'name': "Марійка",'age': 29},
]

'''
with open('data.json', 'w', encoding="UTF-8") as file:
    json.dump(data, file)
    # json.dump(data, file, indent=2)
    # json.dump(data, file, indent=2, ensure_ascii=False)
'''
j = json.dumps(data)
# j = json.dumps(data, indent=2)
j = json.dumps(data, indent=2,  ensure_ascii=False)
print(j)


dict
list, tuple
str
int, float
True, False
None


# Десериализация
with open('data.json', encoding='UTF-8') as file:
    data = json.load(file)
print(data)
