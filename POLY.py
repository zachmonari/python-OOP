#polymorphism
import math
from abc import ABC, abstractmethod

class Shapes(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius **2

class Triangle(Shapes):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5* self.base * self.height

class Rectangle(Shapes):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return  self.width * self.height


shapes=[Circle(7),Triangle(8,6),Rectangle(10,20)]
for shape in shapes:
    print(f"{shape.area()}cm^2")