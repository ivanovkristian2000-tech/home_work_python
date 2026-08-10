"""Проверка размеров фигур

Доработайте фигуры:

Добавьте проверку в конструкторы Circle и Rectangle, чтобы значения были положительными.

Если передано отрицательное или нулевое значение, выбрасывайте пользовательское исключение InvalidSizeError."""


from abc import ABC, abstractmethod
from math import pi


class InvalidSizeError(Exception):
    """Chek right size of shapes"""
    pass


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        if radius > 0:
            self.radius = radius
        else:
            raise InvalidSizeError("Amount must be positive")

    def area(self):
            return pi * (self.radius ** 2)


class Rectangle(Shape):
    def __init__(self, width, height):
        if width >= 0 and height >= 0:
            self.width = width
            self.height = height
        else:
            raise InvalidSizeError("Amount must be positive")

    def area(self):
            return self.width * self.height




shapes = [Circle(3), Rectangle(4, 5)]


for shape in shapes:
    print(f"Area of {type(shape).__name__}: {shape.area():.2f}")




try:
    c = Circle(-3)
except InvalidSizeError as e:
    print("Circle error:", e)

try:
    r = Rectangle(-4, -5)
except InvalidSizeError as e:
    print("Rectangle error:", e)