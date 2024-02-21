'''Анаграма — Слово або словосполучення, утворене переставлянням літер, у результаті чого утворюється інше слово, напр.: автор – тавро.

Створіть функцію is_anagram(), яка приймає два рядки і повертає True, якщо вони є анаграмами, тобто мають однакові символи у різному порядку, і False в іншому випадку.
'''

def is_anagram(s1:str, s2:str)->bool:
    return len(s1) == len(s2) and set(s1.lower()) == set(s2.lower())

# Тести для анаграм
assert is_anagram("listen", "silent") == True
assert is_anagram("evil", "vile") == True
assert is_anagram("heart", "earth") == True
assert is_anagram("debit card", "bad credit") == True
assert is_anagram("listen", "silentt") == False
assert is_anagram("evil", "vile ") == False
assert is_anagram("hello", "world") == False
assert is_anagram("Молоко", "молок") == False
assert is_anagram("python", "java") == False
assert is_anagram("cat", "dog") == False
assert is_anagram("", "") == True
assert is_anagram("", "a") == False
assert is_anagram("a", "") == False
assert is_anagram("Listen", "silent") == True
assert is_anagram("Evil", "vile") == True
assert is_anagram("Heart", "earth") == True
assert is_anagram("Debit card", "bad Credit") == True
