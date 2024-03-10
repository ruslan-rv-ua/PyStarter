def flatten1(l):
    result = []
    for item in l:
        if isinstance(item, list):
            result.extend(flatten1(item))
        else:
            result.append(item)
    return result

def flatten2(l):
    result = []
    while l:
        item = l.pop(0)
        if isinstance(item, list):
            l = item + l
        else:
            result.append(item)
    return result

for flatten in flatten1, flatten2:
    assert flatten([]) == []
    assert flatten([1]) == [1]
    assert flatten([1, 2]) == [1, 2]
    assert flatten([1, [2, 3]]) == [1, 2, 3]
    assert flatten([1, [2, 3], 4]) == [1, 2, 3, 4]
    assert flatten([1, [2, 3], [4, 5]]) == [1, 2, 3, 4, 5]
    assert flatten([1, [2, 3], [4, 5], 6]) == [1, 2, 3, 4, 5, 6]
    assert flatten([1, [2, 3], [4, 5], [6, 7]]) == [1, 2, 3, 4, 5, 6, 7]
    assert flatten([1, [2, 3], [4, 5], [6, 7], 8]) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert flatten([1, [2, 3], [4, 5], [6, 7], [8, 9]]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert flatten([1, [2, 3], [4, 5], [6, 7], [8, 9], 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert flatten([1, [2, [3, [4, [5, [6, [7]]]]]]]) == [1, 2, 3, 4, 5, 6, 7]
