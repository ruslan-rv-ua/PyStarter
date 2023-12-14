"""Слова по довжині.
"The quick brown fox jumps over the lazy dog".

5: brown, jumps, quick.
4: lazy, over.
3: dog, fox, the.
"""
TEXT = "The quick brown fox jumps over the lazy dog"

words_by_length = {}
for word in TEXT.lower().split():
    length = len(word)
    if length not in words_by_length:
        words_by_length[length] = []
    if word not in words_by_length[length]:
        words_by_length[length].append(word)

for length in sorted(words_by_length.keys(), reverse=True):
    words = ", ".join(sorted(words_by_length[length]))
    print(f"{length}: {words}")
