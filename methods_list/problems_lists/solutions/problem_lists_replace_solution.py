"""
Задача: Заміна елементів списку

Напишіть функцію replace(nums, old, new), яка приймає:
nums - список чисел
old - число, яке потрібно замінити
new - число, на яке потрібно замінити
Функція повинна повернути новий список, де всі елементи old замінені на new.
"""
def replace(nums, old, new):
    # ваш код
    new_nums = []
    for num in nums:
        new_nums.append(new if num == old else num)
    return new_nums
    


# тест
assert replace([1,2,3], 1, 1) == [1,2,3]
assert replace([1,2,3], 1, 3) == [3,2,3]
assert replace([1], 1, 3) == [3]
assert replace([1], 1, 1) == [1]

nums = [1, 2, 3, 2, 5, 2]
new_nums = replace(nums, 2, 200)
assert new_nums == [1, 200, 3, 200, 5, 200]
assert nums is not new_nums
