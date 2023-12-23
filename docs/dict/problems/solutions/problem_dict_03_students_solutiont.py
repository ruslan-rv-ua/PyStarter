STUDENTS = [
    {"name": "Ракоїд Борис Іванович", "marks": [2, 2, 3]},
    {"name": "Тягнирядно Богдан Петрович", "marks": [5, 5, 5, 5]},
    {"name": "Непийпиво Пилип Михайлович", "marks": [3, 3, 3, 1]},
    {"name": "Шевченко Світлана Борисівна", "marks": [5, 4, 3, 2, 1]},
    {"name": "Шинкаренко Ігор Михайлович", "marks": [5, 5, 1, 5, 5]},
]

# ваш код з наступного рядка, умова задачі далі
students_marks = {}
for student in STUDENTS:
    last_name, first_name, middle_name = student["name"].split()
    short_name = f"{last_name} {first_name[0]}.{middle_name[0]}."
    students_marks[short_name] = sum(student["marks"]) / len(student["marks"])

for short_name in sorted(students_marks):
    print(f"{short_name} - {students_marks[short_name]:.1f}")

    
'''
"Студенти"

Є список студентів.
Кожен елемент списка — словник з ключами:
- `name` — прізвище, ім'я та по-батькові студента
- `marks` — список оцінок
Усі дані є валідними.
Написати програму, яка виводить у алфавітному порядку список студентів — прізвище та ініціали, середній бал у форматі:
Непийпиво П.М. - 2.5
Ракоїд Б.І. - 2.3
Тягнирядно Б.П. - 5.0
Шевченко С.Б. - 3.0
Шинкаренко І.М. - 4.2
'''

