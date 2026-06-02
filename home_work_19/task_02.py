""" 02 Счётчик букв в словах

Напишите программу, которая
- подсчитывает количество каждой буквы в заданных словах
- и создаёт словарь, где
        ключи — это слова,
        а значения — это ещё один словарь, где
                ключ - это буква,
                а значение - число повторений этой буквы в слове.
Данные:
words = ["anna", "bennet", "john"]

Пример вывода:
{'anna': {'a': 2, 'n': 2}, 'bennet': {'b': 1, 'e': 2, 'n': 2, 't': 1}, 'john': {'j': 1, 'o': 1, 'h': 1, 'n': 1}}

"""

words = ["anna", "bennet", "john"]

res = {}

for word in words:
    char_count = {}
    for char in word:
        char_count[char] = word.count(char)
    res[word] = char_count

print(res)







