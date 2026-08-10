"""Фигуры и площади

Создайте абстрактный класс Shape.

В классе должен быть метод area(), который возвращает площадь фигуры.

Реализуйте два класса:

Circle, который принимает радиус.

Rectangle, который принимает ширину и высоту.


# Пример использования

shapes = [Circle(3), Rectangle(4, 5)]

for shape in shapes:

    print(f"Area: {shape.area():.2f}")
"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height



shapes = [Circle(3), Rectangle(4, 5)]


for shape in shapes:
    print(f"Area of {type(shape).__name__}: {shape.area():.2f}")
