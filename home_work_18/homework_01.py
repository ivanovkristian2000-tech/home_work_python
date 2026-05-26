""" 01 Не уникальные числа

Напишите программу, которая
- находит все числа, встречающиеся более одного раза в списке,
- и выводит их в порядке убывания.

Данные:
numbers = [4, 7, 3, 7, 8, 3, 4, 2, 7, 3, 8, 4]
Пример вывода:
Числа, встречающиеся более одного раза: [8, 7, 4, 3]
"""

numbers = [4, 7, 3, 7, 8, 3, 4, 2, 7, 3, 8, 4]


new_list = []
count = 0

for num in numbers:
    count = numbers.count(num)
    if num not in new_list and count >= 2:
        new_list.append(num)

print("Числа, встречающиеся более одного раза:", sorted(new_list, reverse= True))


new_list = set()

for num in numbers:
    count = numbers.count(num)
    if count >= 2:
        new_list.add(num)

print("Числа, встречающиеся более одного раза:", sorted(new_list, reverse= True))








