"""
Комбинации одежды

Напишите функцию, которая принимает списки типов одежды, цветов и размеров,
а затем генерирует все возможные комбинации
в формате "Clothe - Color - Size".

Данные:
"""

clothes = ["T-shirt", "Jeans", "Jacket"]

colors = ["Red", "Blue", "Black"]

sizes = ["S", "M", "L"]

"""
Пример вывода:

T-shirt - Red - S

T-shirt - Red - M

T-shirt - Red - L

T-shirt - Blue - S

...

Jacket - Black - L
"""
import itertools


def clothing_combinations(clothes, colors, sizes):

    res = itertools.product(clothes, colors, sizes)

    return res

    # for cloth in clothes:
    #     for color in colors:
    #         for size in sizes:
    #             print(f"{cloth} - {color} - {size}")


for cloth, color, size in clothing_combinations(clothes, colors, sizes):
    print(f"{cloth} - {color} - {size}")



