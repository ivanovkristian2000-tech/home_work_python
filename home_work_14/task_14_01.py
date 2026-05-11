""" 01 Число в конце

Напишите программу, которая
- создает новый список.
В него необходимо добавить только те строки из исходного списка,
в которых цифры находятся только в конце.

Данные:
strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
Пример вывода:
Строки с цифрами только в конце: ['apple23', 'grape3']
"""

strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]

new_strings = []

for word in strings:
    for index, char in enumerate(word):
        if char.isdigit():
            tail = word[index:]
            if tail.isdigit():
                new_strings.append(word)

            break


print("Строки с цифрами только в конце:", new_strings)


# result = []
# for word in strings:
#     if word.rstrip('0123456789').isalpha():
#         result.append(word)
#
# print("Строки с цифрами только в конце:", result)