# geometry.py
import math

def square_area(side_length: float) -> float:
    return side_length ** 2


def rectangle_area(base_length: float, height: float) -> float:
    return base_length * height


def triangle_area(base_length: float, height: float) -> float:
    return (base_length * height) / 2


def circle_area(radius: float) -> float:
    return math.pi * radius ** 2
