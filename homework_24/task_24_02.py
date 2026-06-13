""" 02 Сумма вложенных чисел

Напишите рекурсивную функцию, которая суммирует все числа во вложенных списках.

Попробуйте решить в двух вариантах: tail и non-tail.

Данные:
nested_numbers = [1, [2, 3], [4, [5, 6]], 7]
Пример вывода:
28
"""

def non_tail(lst):
    res = 0
    for num in lst:
        if isinstance(num, list):
            res += non_tail(num)
        else:
            res += num

    return res



print(non_tail([1, [2, 3], [4, [5, 6]], 7]))



def tail(lst, count=0):
    if not lst:
        return count
    first = lst[0]
    rest = lst[1:]
    if isinstance(first, list):
        tail(first)
    else:
        count += first







