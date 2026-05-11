""" 02 Повторяющиеся элементы

Напишите программу, которая
- находит индексы элементов тюпла, встречающихся более одного раза.
- Вывести сами элементы и их индексы.

Данные:
numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
Пример вывода:
Индексы элемента 2: 	1 4 9
Индексы элемента 3: 	2 6
Индексы элемента 4: 	3 8
"""


numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)

count = 0
printed_numbers = ()

for num in numbers:         # считает количество элементов
    count = numbers.count(num)

    if num not in printed_numbers and count >= 2:       # проверяет на уникальность и num >= 2
        printed_numbers += (num,)
        indexes = ""
        for index, value in enumerate(numbers):
            if value == num:
                indexes += str(index) + " "
        print(f"Индексы элемента {num}:     {indexes}")
