""" 02 Зеркальное subset

Напишите программу, которая
- проверяет, являются ли элементы одного из set subset другого.

В случае положительного ответа возвращает разницу между двумя set.

Проверить необходимо в обе стороны.

Данные:
set1 = {2, 3, 4, 5, 6}
set2 = {4, 5}

Пример вывода:
Подмножество: True
Разница: {2, 3, 6}
=====================
Данные:
set1 = {2, 3, 4, 5, 6}
set2 = {4, 7}

Пример вывода:
Подмножество: False
"""

set1 = {2, 3, 4, 5, 6}
set2 = {4, 5}

if set2 <= set1:
    print("Subset:", True)
    print("Разница:", set1 - set2, '\n')
else:
    print("Subset:", False)


set1 = {2, 3, 4, 5, 6}
set2 = {4, 7}

if set2 <= set1:
    print("Subset:", True)
    print("Разница:", set1 - set2, '\n')
else:
    print("Subset:", False)


set1 = {2, 3, 4, 5, 6}
set2 = {4, 5}

res = set()
dif = set()

for s in set1:
    if s in set2:
        res.add(s)
    else:
        dif.add(s)

if res == set2:
    print("Subset:", True)
    print("Разница:", dif)
else:
    print("Subset:", False)