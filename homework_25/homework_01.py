""" 01 Деление без ошибок

Напишите функцию, которая
- выполняет деление двух чисел, введенных пользователем,
- и обрабатывает возможные ошибки.

ВАЖНО: Используйте несколько обработок различных ошибок

Примеры вывода:

Введите делимое: 345
Введите делитель: 5a
Ошибка: Введено некорректное число.

Введите делимое: 5
Введите делитель: 0
Ошибка: Деление на ноль невозможно.

Введите делимое: 5
Введите делитель: 2
Результат: 2.5

"""

def safe_division(dividend, divisor):

    dividend = float(dividend)
    divisor = float(divisor)

    res = dividend / divisor
    print(res)



try:
    safe_division('a', 5)       # False
    # safe_division(5, 0)         # False
    # safe_division(5, 2)         # True
    # safe_division('5.5', '1.2') # True

except TypeError:
    print("Ошибка: Введено некорректное число.")

except ValueError:
    print("Ошибка: Введено некорректное число.")

except ZeroDivisionError:
    print("Деление на ноль невозможно.")


