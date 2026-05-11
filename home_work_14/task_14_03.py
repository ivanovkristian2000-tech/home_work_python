""" 3. Порядок чётных

Напишите программу, которая
- формирует новый список чисел.

Добавьте в него все элементы исходного списка, где:
- нечетные числа занимают те же позиции,
- чётные числа отсортированы между собой обратном порядке.

Данные:
numbers = [5, 2, 3, 8, 4, 1, 2, 7]
Пример вывода:
Список после сортировки: [5, 8, 3, 4, 2, 1, 2, 7]
"""

numbers = [5, 2, 3, 8, 4, 1, 2, 7]

new_numbers = []
even_numbers = []

for num in numbers:         # берем четное сортируем и переворачиваем.
    if num % 2 == 0:
        even_numbers.append(num)
even_numbers.sort(reverse=True)


for num in numbers:         # идем по не четным и вставляем в список.
    if num % 2 != 0:
        new_numbers.append(num)

    else:                   # если четное удаляем и сохраняем по 0 index и добавляем в список.
        largest_even = even_numbers.pop(0)
        new_numbers.append(largest_even)

print("Список после сортировки: ", new_numbers)